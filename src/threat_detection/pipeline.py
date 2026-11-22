"""End-to-end wiring: Segment -> detectors -> fusion -> temporal alert."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from threat_detection.alerts.temporal import PersistenceAlerter
from threat_detection.fusion.threat_score import FusedResult, fuse
from threat_detection.types import Detector, DetectorOutput, Segment


@dataclass
class PipelineResult:
    timestamp: float
    outputs: list[DetectorOutput]
    fused: FusedResult
    alert: bool


class ThreatPipeline:
    def __init__(
        self,
        detectors: Sequence[Detector],
        alerter: PersistenceAlerter,
        weights: dict[str, float] | None = None,
        min_confidence: float = 0.3,
        fusion_mode: str = "max",
    ) -> None:
        self.detectors = list(detectors)
        self.alerter = alerter
        self.weights = weights
        self.min_confidence = min_confidence
        self.fusion_mode = fusion_mode

    def process_segment(self, segment: Segment) -> PipelineResult:
        outputs = [d.predict(segment) for d in self.detectors]
        fused = fuse(outputs, self.weights, self.min_confidence, self.fusion_mode)
        alert = self.alerter.update(fused.score, segment.end)
        return PipelineResult(timestamp=segment.end, outputs=outputs, fused=fused, alert=alert)
