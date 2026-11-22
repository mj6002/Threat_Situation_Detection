"""Shared data contracts.

Every detector takes a Segment and returns a DetectorOutput. Keep these stable:
both of us build against them. Discuss in an issue before changing anything here.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Segment:
    """A short window of sampled video (for example 3 seconds)."""

    frames: list[Any]                 # list of BGR numpy arrays (H, W, 3)
    timestamps: list[float]           # seconds from video start, one per frame
    tracks: Any | None = None      # filled by the tracking stage
    poses: Any | None = None       # filled by the pose stage

    @property
    def start(self) -> float:
        return self.timestamps[0]

    @property
    def end(self) -> float:
        return self.timestamps[-1]


@dataclass(frozen=True)
class DetectorOutput:
    """Result of one threat detector on one Segment."""

    name: str                         # "violence" | "harassment_risk" | "crowd"
    score: float                      # 0..1, likelihood of a threat situation
    confidence: float                 # 0..1, how much to trust the score
    meta: dict[str, Any] = field(default_factory=dict)  # explanation / debug info

    def __post_init__(self) -> None:
        if not 0.0 <= self.score <= 1.0:
            raise ValueError(f"score must be in [0, 1], got {self.score}")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(f"confidence must be in [0, 1], got {self.confidence}")


class Detector(ABC):
    """Base class for the three threat detectors."""

    name: str = "detector"

    @abstractmethod
    def predict(self, segment: Segment) -> DetectorOutput:
        """Return a score and confidence for this segment."""
