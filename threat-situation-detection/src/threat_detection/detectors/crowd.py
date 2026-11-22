"""Crowd density + optical-flow stampede-condition detector.  TODO: Weeks 2-4.

Works on raw frames, so it does not depend on the tracking stage and can be built first.
"""
from threat_detection.types import Detector, DetectorOutput, Segment


class CrowdDetector(Detector):
    name = "crowd"

    def predict(self, segment: Segment) -> DetectorOutput:
        raise NotImplementedError("Optical flow: speed rise, flow divergence, directional entropy")
