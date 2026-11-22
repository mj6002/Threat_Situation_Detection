"""Person detection (YOLOv8).  TODO: see docs/TASKS.md, Week 2."""
from __future__ import annotations

from typing import Any


class PersonDetector:
    def __init__(self, weights: str = "yolov8n.pt", conf: float = 0.4) -> None:
        self.weights = weights
        self.conf = conf

    def detect(self, frame: Any) -> list[Any]:
        """Return person boxes for one frame, as [x1, y1, x2, y2, confidence]."""
        raise NotImplementedError("Week 2: load YOLOv8 and filter to the 'person' class")
