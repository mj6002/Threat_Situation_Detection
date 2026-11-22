# Computer Vision Based Detection of Threat Situations for Public and Women's Safety

A video-analysis pipeline that flags three kinds of threat situations for **human review**:

1. **Violence / abuse** between people (action recognition)
2. **Harassment-risk interaction patterns** (rule-based, from tracking and pose; it detects *risk patterns*, it does not confirm harassment)
3. **Stampede-prone crowd conditions** (crowd density + optical flow)

Final-year minor project, MBM University, Jodhpur. Team: Manan Jain, [friend's name].

> This is an alerting aid. It does no identity recognition and makes no automatic enforcement decisions.

## How it works

```
video -> frame sampler -> person detection -> tracking -> pose + motion features
                                   |                              |
                                   +--> crowd analysis            +--> violence detector
                                   |                              +--> harassment-risk module
                                   v                              v
                              threat score fusion -> temporal persistence -> alert log / dashboard
```

All three detectors share one contract (`src/threat_detection/types.py`): they take a `Segment` of sampled frames and return a `DetectorOutput(score, confidence)`. That is what lets two people build different detectors without blocking each other. Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Quick start

```bash
git clone <repo-url> && cd threat-situation-detection
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt                      # light: enough to run tests
pip install -r requirements.txt                          # OpenCV, pandas, scikit-learn
pip install -r requirements-ml.txt                       # only when working on models/dashboard
pytest
```

`pytest` should pass on a fresh clone. If it does not, tell the other person before doing anything else.

## Repo map

| Path | What lives there |
|---|---|
| `src/threat_detection/types.py` | Shared contracts (`Segment`, `DetectorOutput`, `Detector`). Change only after discussing in an issue |
| `src/threat_detection/io/` | Video reading and frame sampling |
| `src/threat_detection/detection/`, `tracking/`, `features/` | Person detection, tracking, pose and motion features |
| `src/threat_detection/detectors/` | The three threat detectors |
| `src/threat_detection/fusion/`, `alerts/` | Score fusion and temporal persistence |
| `src/threat_detection/evaluation/` | Metrics (false alarms per hour etc.) |
| `configs/default.yaml` | Thresholds and weights, so tuning needs no code change |
| `tests/` | Unit tests |
| `data/` | Local only, never committed ([data/README.md](data/README.md)) |
| `docs/` | Architecture, datasets, task list |

## Status

| Module | Owner | Status |
|---|---|---|
| Fusion, temporal alerts, pipeline wiring | both | baseline done, tested |
| Frame sampling | A | done |
| Person detection, tracking, pose | A | todo |
| Violence detector | A | todo |
| Crowd / stampede detector | B | todo |
| Harassment-risk module | B | todo |
| Dashboard + SQLite alert log | B | todo |
| Evaluation | both | partial |

Update this table in the same PR that changes a module's status.

## Working together

Read [CONTRIBUTING.md](CONTRIBUTING.md) (short). The task list with weekly milestones is in [docs/TASKS.md](docs/TASKS.md). GitHub setup and contribution tracking: [docs/GITHUB_SETUP.md](docs/GITHUB_SETUP.md).
