#!/usr/bin/env bash
# Creates the starter issues. Requires the GitHub CLI: https://cli.github.com  (run `gh auth login` first).
set -euo pipefail
issues=(
  "Set up environment and confirm pytest passes on both machines"
  "Dataset inspection and licence checklist (docs/DATASETS.md)"
  "Implement PersonDetector (YOLOv8, person class only)"
  "Implement track_people (ByteTrack)"
  "Implement pose and motion feature extraction"
  "Implement CrowdDetector (optical-flow features)"
  "Fine-tune ViolenceDetector on RWF-2000"
  "Implement HarassmentRiskDetector rules"
  "Record consented staged clips for harassment-risk validation"
  "Evaluation harness: per-class precision/recall/F1, false alarms per hour, inference time"
  "SQLite alert log and Streamlit review dashboard"
  "Ablation: baseline vs pose features vs temporal smoothing; max vs weighted-mean fusion"
)
for title in "${issues[@]}"; do
  gh issue create --title "$title" --body "See docs/TASKS.md for context and owner." --label task || \
  gh issue create --title "$title" --body "See docs/TASKS.md for context and owner."
done
