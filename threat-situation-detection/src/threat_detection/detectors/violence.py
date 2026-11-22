"""Violence / abuse detector (fine-tuned action-recognition model).  TODO: Week 3."""
from threat_detection.types import Detector, DetectorOutput, Segment


class ViolenceDetector(Detector):
    name = "violence"

    def predict(self, segment: Segment) -> DetectorOutput:
        raise NotImplementedError("Week 3: fine-tune on RWF-2000, return violence probability")
