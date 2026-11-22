"""Combine detector outputs into one threat score."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from threat_detection.types import DetectorOutput


@dataclass(frozen=True)
class FusedResult:
    score: float
    uncertain: bool                   # True when no detector was confident enough
    top_detector: str | None
    used: list[str]


def fuse(
    outputs: Sequence[DetectorOutput],
    weights: dict[str, float] | None = None,
    min_confidence: float = 0.3,
    mode: str = "max",
) -> FusedResult:
    """Fuse detector scores.

    mode="max": strongest weighted signal wins (a single strong detector can raise an alert).
    mode="weighted_mean": weighted average (smoother, but can dilute one strong signal).
    Outputs below `min_confidence` are ignored; if all are ignored the result is marked uncertain.
    """
    weights = weights or {}
    kept = [o for o in outputs if o.confidence >= min_confidence]
    if not kept:
        return FusedResult(score=0.0, uncertain=True, top_detector=None, used=[])

    weighted = [(o.name, weights.get(o.name, 1.0) * o.score, weights.get(o.name, 1.0)) for o in kept]
    top = max(weighted, key=lambda x: x[1])
    if mode == "max":
        score = top[1]
    elif mode == "weighted_mean":
        score = sum(w_s for _, w_s, _ in weighted) / sum(w for _, _, w in weighted)
    else:
        raise ValueError(f"unknown mode: {mode}")
    return FusedResult(score=min(1.0, score), uncertain=False, top_detector=top[0], used=[n for n, _, _ in weighted])
