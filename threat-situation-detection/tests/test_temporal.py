from threat_detection.alerts.temporal import PersistenceAlerter


def test_needs_consecutive_hits():
    a = PersistenceAlerter(threshold=0.6, min_consecutive=3, cooldown_seconds=10)
    assert [a.update(0.9, t) for t in (0, 1)] == [False, False]
    assert a.update(0.9, 2) is True


def test_streak_resets_when_score_drops():
    a = PersistenceAlerter(threshold=0.6, min_consecutive=3, cooldown_seconds=10)
    a.update(0.9, 0)
    a.update(0.9, 1)
    a.update(0.1, 2)
    assert a.update(0.9, 3) is False


def test_cooldown_blocks_repeat_alerts():
    a = PersistenceAlerter(threshold=0.6, min_consecutive=1, cooldown_seconds=10)
    assert a.update(0.9, 0) is True
    assert a.update(0.9, 5) is False
    assert a.update(0.9, 11) is True
