import React from "react";
import { Composition } from "remotion";
import { Short } from "./Short";
import shots from "../../episodes/001-tortoise-hare/shots.json";

const last = shots.shots[shots.shots.length - 1];
const FPS = shots.format.fps;
const DURATION = Math.round((last.t + last.dur) * FPS);

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="Short-EN"
      component={Short}
      durationInFrames={DURATION}
      fps={FPS}
      width={shots.format.w}
      height={shots.format.h}
      defaultProps={{ lang: "en" as const }}
    />
    <Composition
      id="Short-GR"
      component={Short}
      durationInFrames={DURATION}
      fps={FPS}
      width={shots.format.w}
      height={shots.format.h}
      defaultProps={{ lang: "gr" as const }}
    />
  </>
);
