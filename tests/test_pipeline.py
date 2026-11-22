from threat_detection.alerts.temporal import PersistenceAlerter
from threat_detection.pipeline import ThreatPipeline
from threat_detection.types import Detector, DetectorOutput, Segment


class FakeDetector(Detector):
    name = "violence"

    def __init__(self, score):
        self.score = score

    def predict(self, segment):
        return DetectorOutput(name=self.name, score=self.score, confidence=0.9)


def make_segment(t):
    return Segment(frames=[], timestamps=[t])


def test_alert_after_persistent_threat():
    p = ThreatPipeline([FakeDetector(0.9)], PersistenceAlerter(0.6, 2, 5))
    assert p.process_segment(make_segment(1.0)).alert is False
    assert p.process_segment(make_segment(2.0)).alert is True
