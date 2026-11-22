"""Evaluation helpers. Per-class precision/recall/F1: use sklearn.metrics directly."""
from __future__ import annotations

from collections.abc import Sequence


def false_alarms_per_hour(
    alert_times: Sequence[float],
    true_event_windows: Sequence[tuple[float, float]],
    video_hours: float,
) -> float:
    """Alerts that fall outside every true-event window, divided by video duration in hours."""
    if video_hours <= 0:
        raise ValueError("video_hours must be positive")
    false_alerts = [t for t in alert_times if not any(s <= t <= e for s, e in true_event_windows)]
    return len(false_alerts) / video_hours
