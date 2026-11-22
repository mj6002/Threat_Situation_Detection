"""Harassment-RISK pattern detector (rule-based, from tracks + pose).  TODO: Week 5.

This module detects risk patterns (rapid approach, surrounding geometry, one person
retreating). It does NOT confirm harassment. Keep that wording everywhere.
"""
from threat_detection.types import Detector, DetectorOutput, Segment


class HarassmentRiskDetector(Detector):
    name = "harassment_risk"

    def predict(self, segment: Segment) -> DetectorOutput:
        raise NotImplementedError("Week 5: needs segment.tracks and segment.poses")
