# Tasks and weekly plan

A = Manan, B = friend. Swap if strengths differ, but keep one owner per module.

**Parallelism note:** the crowd detector works on raw frames and does not need tracking, so B can start it in Week 1 while A builds detection and tracking.

| Week | A | B |
|---|---|---|
| 1 | Environment, repo, dataset inspection and licence checks | Same repo setup; start crowd detector: read frames, compute optical flow |
| 2 | Person detection (YOLOv8), tracking (ByteTrack), pose extraction | Crowd features: speed rise, flow divergence, directional entropy |
| 3 | Fine-tune violence detector on RWF-2000, per-class metrics | Crowd/stampede evaluation on crowd datasets |
| 4 | Violence error analysis, threshold calibration | Harassment-risk rules (needs tracks + pose from Week 2) |
| 5 | Evaluation harness, false alarms per hour | Fusion tuning, record consented staged clips |
| 6 | Integration test on recorded videos | Streamlit dashboard + SQLite alert log |
| Final | Evaluation, report, viva prep | Evaluation, report, viva prep |

## Starter issues

Create these on GitHub (or run `scripts/create_issues.sh`):

1. Set up environment and confirm `pytest` passes on both machines
2. Dataset inspection and licence checklist (docs/DATASETS.md)
3. Implement `PersonDetector` (YOLOv8, person class only)
4. Implement `track_people` (ByteTrack)
5. Implement pose and motion feature extraction
6. Implement `CrowdDetector` (optical-flow features)
7. Fine-tune `ViolenceDetector` on RWF-2000
8. Implement `HarassmentRiskDetector` rules
9. Record consented staged clips for harassment-risk validation
10. Evaluation harness: per-class precision/recall/F1, false alarms per hour, inference time
11. SQLite alert log and Streamlit review dashboard
12. Ablation: baseline vs pose features vs temporal smoothing; max vs weighted-mean fusion
