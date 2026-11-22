"""Multi-object tracking (ByteTrack).  TODO: see docs/TASKS.md, Week 2."""
from __future__ import annotations

from typing import Any

from threat_detection.types import Segment


def track_people(segment: Segment, detector: Any) -> Segment:
    """Run detection + tracking over a Segment and set `segment.tracks`.

    Expected format for segment.tracks: {track_id: [(timestamp, x1, y1, x2, y2), ...]}
    """
    raise NotImplementedError("Week 2: use ultralytics tracking with ByteTrack")
