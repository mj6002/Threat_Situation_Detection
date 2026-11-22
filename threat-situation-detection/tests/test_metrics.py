from threat_detection.evaluation.metrics import false_alarms_per_hour


def test_false_alarms_per_hour():
    assert false_alarms_per_hour([10, 500, 900], [(0, 20)], video_hours=0.5) == 4.0
