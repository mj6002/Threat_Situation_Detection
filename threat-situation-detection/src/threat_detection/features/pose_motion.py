"""Pose keypoints and motion features per tracked person.  TODO: Week 2."""
from __future__ import annotations

from threat_detection.types import Segment


def extract_pose_motion(segment: Segment) -> Segment:
    """Set `segment.poses`: {track_id: [(timestamp, keypoints), ...]} and derived speeds/distances."""
    raise NotImplementedError("Week 2: YOLOv8-pose or MediaPipe")
