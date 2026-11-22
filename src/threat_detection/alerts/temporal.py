"""Temporal persistence: raise an alert only if a threat score persists."""
from __future__ import annotations


class PersistenceAlerter:
    """Fires when score >= threshold for `min_consecutive` updates in a row.

    After firing, stays quiet for `cooldown_seconds` to avoid repeated alerts for one event.
    """

    def __init__(self, threshold: float = 0.6, min_consecutive: int = 3, cooldown_seconds: float = 30.0) -> None:
        self.threshold = threshold
        self.min_consecutive = min_consecutive
        self.cooldown_seconds = cooldown_seconds
        self._streak = 0
        self._last_alert: float | None = None

    def update(self, score: float, timestamp: float) -> bool:
        if score >= self.threshold:
            self._streak += 1
        else:
            self._streak = 0
        if self._streak < self.min_consecutive:
            return False
        if self._last_alert is not None and timestamp - self._last_alert < self.cooldown_seconds:
            return False
        self._last_alert = timestamp
        return True
