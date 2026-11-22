# Architecture

## Data flow

1. **Frame sampler** (`io/video.py`): reads a video and groups sampled frames into `Segment`s (about 3 s).
2. **Person detection + tracking** (`detection/`, `tracking/`): fills `segment.tracks` as `{track_id: [(t, x1, y1, x2, y2), ...]}`.
3. **Pose + motion features** (`features/`): fills `segment.poses`.
4. **Detectors** (`detectors/`): each returns a `DetectorOutput`.
   - `violence`: action-recognition model on the frames (or pose sequences).
   - `harassment_risk`: rules on tracks + pose (approach speed, surrounding, one person retreating).
   - `crowd`: density and optical-flow features on raw frames. Independent of tracking, so it can be built first.
5. **Fusion** (`fusion/threat_score.py`): combines outputs. Default `max` mode so one strong detector can raise an alert; `weighted_mean` is available for comparison (ablation).
6. **Temporal persistence** (`alerts/temporal.py`): alert only after N consecutive high scores, then a cooldown.
7. **Alert log + dashboard**: SQLite + Streamlit, for human review.

## Contracts

```python
Segment(frames, timestamps, tracks=None, poses=None)
DetectorOutput(name, score, confidence, meta={})   # score and confidence in [0, 1]
Detector.predict(segment) -> DetectorOutput
```

## Design decisions to record here

When you make a decision that the other person needs to know (threshold, model choice, dataset split), add a dated line below.

- (empty)
