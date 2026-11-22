import pytest

from threat_detection.fusion.threat_score import fuse
from threat_detection.types import DetectorOutput


def out(name, score, conf=1.0):
    return DetectorOutput(name=name, score=score, confidence=conf)


def test_max_mode_keeps_single_strong_signal():
    r = fuse([out("violence", 0.9), out("crowd", 0.1)], mode="max")
    assert r.score == pytest.approx(0.9) and r.top_detector == "violence"


def test_weighted_mean_dilutes():
    r = fuse([out("violence", 0.9), out("crowd", 0.1)], mode="weighted_mean")
    assert r.score == pytest.approx(0.5)


def test_low_confidence_outputs_are_ignored_and_marked_uncertain():
    r = fuse([out("violence", 0.9, conf=0.1)], min_confidence=0.3)
    assert r.uncertain and r.score == 0.0


def test_detector_output_validates_range():
    with pytest.raises(ValueError):
        DetectorOutput(name="x", score=1.5, confidence=0.5)
