#!/usr/bin/env python3
"""
Assemble prompts from the style bible and generate key frames via fal.ai.

The whole point is that nothing here invents style. Every fixed block is read
verbatim from brand/prompt-kit.md and brand/characters/owl.md at run time, so a
frame generated in six months is assembled from the same words as one generated
today. If the look drifts, the bible changed — not this script.

Usage:
    python3 pipeline/generate_stills.py 001-tortoise-hare            # all shots
    python3 pipeline/generate_stills.py 001-tortoise-hare 1 12       # named shots
    python3 pipeline/generate_stills.py 001-tortoise-hare 1 --n 3    # 3 variants
"""

import base64, json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL = "fal-ai/recraft/v3/text-to-image"

# Recraft V3 is the closest model to this brief: it has a native
# vector_illustration style and accepts a brand colour array. It has no
# negative-prompt parameter, so the constraints live in the style preamble.
STYLE = "vector_illustration"


# ---------- reading the bible ----------

def fences(text):
    return re.findall(r"```\n(.*?)```", text, re.S)


def load_prompt_kit():
    t = (ROOT / "brand/prompt-kit.md").read_text()
    sections = re.split(r"\n## ", t)

    def sect(prefix):
        for s in sections:
            if s.startswith(prefix):
                return s
        raise SystemExit(f"prompt-kit.md: missing section '{prefix}'")

    preamble = fences(sect("1. Style preamble"))[0].strip()
    plane = fences(sect("3. Plane brief"))[0].strip()

    keys = {}
    keysect = sect("2. Scene key fragments")
    for name, body in re.findall(r"\*\*([a-z-]+)\*\*.*?\n```\n(.*?)```", keysect, re.S):
        keys[name] = body.strip()

    return preamble, plane, keys


def load_owl():
    t = (ROOT / "brand/characters/owl.md").read_text()
    for s in re.split(r"\n## ", t):
        if s.startswith("8. Prompt block"):
            return fences(s)[0].strip()
    raise SystemExit("owl.md: missing section '8. Prompt block'")


def load_colors():
    tok = json.loads((ROOT / "brand/tokens.json").read_text())
    out = {}
    for name, spec in tok["core"].items():
        h = spec["hex"].lstrip("#")
        out[name] = {"r": int(h[0:2], 16), "g": int(h[2:4], 16), "b": int(h[4:6], 16)}
    return out


SCENE_PALETTE = {
    "midday-white": ["bone", "sun", "aegean", "terracotta", "ink"],
    "dusk-violet":  ["plum", "terracotta", "sun", "ink", "bone"],
    "olive-shade":  ["olive", "seafoam", "bone", "sun", "ink"],
    "storm-grey":   ["storm", "ink", "bone", "sun", "aegean"],
    "hearth-amber": ["terracotta", "sun", "bone", "ink"],
    "sea-deep":     ["deepsea", "aegean", "seafoam", "bone", "sun"],
}


def build_prompt(shot, preamble, plane, keys, owl):
    key = shot["scene_key"]
    if key not in keys:
        raise SystemExit(f"shot {shot['id']}: unknown scene key '{key}'")
    parts = [preamble, keys[key], plane]
    if shot.get("owl"):
        parts.append(owl)
    parts.append(shot["subject"])
    return "\n\n".join(parts)


def palette_for(shot, colors):
    names = list(SCENE_PALETTE[shot["scene_key"]])
    if shot.get("owl") and "plum" not in names:
        names.append("plum")
    return [colors[n] for n in names]


# ---------- fal.ai ----------

def fal(path, payload=None, method="GET"):
    key = os.environ.get("FAL_KEY")
    if not key:
        raise SystemExit("FAL_KEY not set — run: set -a && source .env && set +a")
    req = urllib.request.Request(
        path, method=method,
        data=json.dumps(payload).encode() if payload else None,
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"fal {e.code}: {e.read().decode()[:400]}")


def generate(prompt, colors, w, h):
    sub = fal(f"https://queue.fal.run/{MODEL}", {
        "prompt": prompt,
        "image_size": {"width": w, "height": h},
        "style": STYLE,
        "colors": colors,
    }, "POST")
    status_url, resp_url = sub["status_url"], sub["response_url"]
    for _ in range(120):
        time.sleep(2)
        st = fal(status_url)
        if st.get("status") == "COMPLETED":
            return fal(resp_url)
        if st.get("status") in ("FAILED", "CANCELLED"):
            raise SystemExit(f"generation {st.get('status')}: {st}")
    raise SystemExit("timed out waiting for fal")


def download(url, dest):
    with urllib.request.urlopen(url, timeout=120) as r:
        dest.write_bytes(r.read())


# ---------- main ----------

def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        raise SystemExit(__doc__)
    episode = args[0]
    n = 1
    if "--n" in args:
        i = args.index("--n"); n = int(args[i + 1]); del args[i:i + 2]
    wanted = {int(a) for a in args[1:] if a.isdigit()}

    epdir = ROOT / "episodes" / episode
    shots = json.loads((epdir / "shots.json").read_text())
    fmt = shots["format"]
    outdir = epdir / "frames"; outdir.mkdir(parents=True, exist_ok=True)

    preamble, plane, keys = load_prompt_kit()
    owl = load_owl()
    colors = load_colors()

    todo = [s for s in shots["shots"] if not wanted or s["id"] in wanted]
    print(f"{episode}: {len(todo)} shot(s), {n} variant(s) each, {fmt['w']}x{fmt['h']}")
    print(f"model {MODEL} · style {STYLE}\n")

    log = []
    for shot in todo:
        prompt = build_prompt(shot, preamble, plane, keys, owl)
        pal = palette_for(shot, colors)
        for v in range(1, n + 1):
            tag = f"shot{shot['id']:02d}" + (f"_v{v}" if n > 1 else "")
            print(f"  {tag}  [{shot['scene_key']}]{'  OWL' if shot.get('owl') else ''}")
            res = generate(prompt, pal, fmt["w"], fmt["h"])
            for img in res.get("images", []):
                dest = outdir / f"{tag}.png"
                download(img["url"], dest)
                print(f"    -> {dest.relative_to(ROOT)}  ({dest.stat().st_size // 1024} KB)")
                log.append({"shot": shot["id"], "variant": v, "file": dest.name,
                            "scene_key": shot["scene_key"], "prompt": prompt})

    (outdir / "generation-log.json").write_text(json.dumps(log, indent=2))
    print(f"\ndone — {len(log)} image(s). Prompts recorded in frames/generation-log.json")


if __name__ == "__main__":
    main()
