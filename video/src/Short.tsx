import React from "react";
import {
  AbsoluteFill, Sequence, Img, staticFile,
  useCurrentFrame, useVideoConfig, interpolate, Easing,
} from "remotion";
import shots from "../../episodes/001-tortoise-hare/shots.json";
import tokens from "../../brand/tokens.json";

// Scene keys drive the ground colour when a generated background is absent, so
// the film is always watchable end to end even before every frame is generated.
const GROUND: Record<string, string> = Object.fromEntries(
  Object.entries(tokens.sceneKeys).map(([k, v]: [string, any]) => [k, v.ground])
);
const RAMP: Record<string, string[]> = Object.fromEntries(
  Object.entries(tokens.sceneKeys).map(([k, v]: [string, any]) => [k, v.ramp])
);

type Cast = { who: string; x: number; y: number; scale: number; drift?: number[]; rot?: number };

/** Flat depth planes standing in for an unrendered background. Deliberately
 *  simple: sky, far hills, ground, and a cropped foreground mass — the same
 *  five-plane structure the prompt kit asks the model for. */
const PlaceholderPlanes: React.FC<{ sceneKey: string; t: number }> = ({ sceneKey, t }) => {
  const ramp = RAMP[sceneKey] ?? ["#F7F1E4", "#F2B33D", "#1F5FA8", "#D0603C", "#23212B"];
  return (
    <AbsoluteFill style={{ backgroundColor: ramp[0] }}>
      <div style={{
        position: "absolute", left: `${-8 + t * 2}%`, top: "34%", width: "130%", height: "40%",
        backgroundColor: ramp[2], borderRadius: "50% 50% 0 0 / 70% 70% 0 0", opacity: 0.9,
      }} />
      <div style={{
        position: "absolute", left: `${-14 + t * 5}%`, top: "48%", width: "150%", height: "44%",
        backgroundColor: ramp[3], borderRadius: "44% 56% 0 0 / 60% 60% 0 0",
      }} />
      <div style={{
        position: "absolute", left: 0, bottom: 0, width: "100%", height: "26%",
        backgroundColor: ramp[1],
      }} />
      {/* P4 — cropped foreground, the plane that sells the depth */}
      <div style={{
        position: "absolute", left: `${-18 + t * 14}%`, bottom: "-9%",
        width: "58%", height: "26%", backgroundColor: ramp[4], borderRadius: "50%",
      }} />
      <div style={{
        position: "absolute", right: `${-22 + t * 10}%`, bottom: "-12%",
        width: "50%", height: "22%", backgroundColor: ramp[4], borderRadius: "50%",
      }} />
    </AbsoluteFill>
  );
};

const Shot: React.FC<{ shot: any }> = ({ shot }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const dur = shot.dur * fps;

  // 0 -> 1 across the shot, eased, driving every camera move.
  const t = interpolate(frame, [0, dur], [0, 1], {
    extrapolateRight: "clamp", easing: Easing.inOut(Easing.ease),
  });

  // Hold the first and last beats a touch longer before moving.
  const zoom = 1.06 + t * 0.07;
  const bgFile = shot.plate as string | undefined;

  return (
    <AbsoluteFill style={{ backgroundColor: GROUND[shot.scene_key] ?? "#F7F1E4", overflow: "hidden" }}>
      {bgFile ? (
        <AbsoluteFill style={{
          transform: `scale(${zoom}) translateX(${(t - 0.5) * -2.2}%)`,
          transformOrigin: "center center",
        }}>
          <Img src={staticFile(`frames/${bgFile}.svg`)}
               style={{ width: "100%", height: "100%", objectFit: "cover" }} />
        </AbsoluteFill>
      ) : (
        <AbsoluteFill style={{ transform: `scale(${zoom})`, transformOrigin: "center center" }}>
          <PlaceholderPlanes sceneKey={shot.scene_key} t={t} />
        </AbsoluteFill>
      )}

      {(shot.cast as Cast[]).map((c, i) => {
        const dx = (c.drift?.[0] ?? 0) * t;
        const dy = (c.drift?.[1] ?? 0) * t;
        // Characters sit on the subject plane and move faster than the mid ground.
        const bob = Math.sin((frame / fps) * 2.4 + i) * 0.35;
        return (
          <Img
            key={i}
            src={staticFile(`cast/${c.who}.svg`)}
            style={{
              position: "absolute",
              left: `${c.x + dx}%`,
              top: `${c.y + dy + bob}%`,
              transform: `translate(-50%, -50%) scale(${c.scale}) rotate(${c.rot ?? 0}deg)`,
              transformOrigin: "center center",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

const Subtitle: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 190 }}>
      <div style={{
        opacity: o,
        maxWidth: "82%",
        textAlign: "center",
        fontFamily: "Nunito, system-ui, sans-serif",
        fontWeight: 800,
        fontSize: 50,
        lineHeight: 1.24,
        letterSpacing: "-0.5px",
        color: tokens.core.bone.hex,
        padding: "20px 34px",
        borderRadius: 26,
        backgroundColor: tokens.core.ink.hex,
        boxShadow: `0 10px 0 ${tokens.core.ink.hex}33`,
      }}>{text}</div>
    </AbsoluteFill>
  );
};

export const Short: React.FC<{ lang?: "en" | "gr" }> = ({ lang = "en" }) => {
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ backgroundColor: tokens.core.ink.hex }}>
      {shots.shots.map((shot: any) => (
        <Sequence key={shot.id} from={Math.round(shot.t * fps)}
                  durationInFrames={Math.round(shot.dur * fps)}>
          <Shot shot={shot} />
          <Subtitle text={shot.narration[lang]} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
