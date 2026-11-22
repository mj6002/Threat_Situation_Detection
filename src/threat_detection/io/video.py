"""Video reading and frame sampling."""
from __future__ import annotations

from collections.abc import Iterator

from threat_detection.types import Segment


def sample_frames(path: str, every_seconds: float = 0.5) -> Iterator[tuple[float, object]]:
    """Yield (timestamp_seconds, frame) roughly every `every_seconds` from a video file."""
    import cv2  # imported lazily so tests run without OpenCV

    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise OSError(f"Cannot open video source: {path}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    step = max(1, round(fps * every_seconds))
    index = 0
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if index % step == 0:
                yield index / fps, frame
            index += 1
    finally:
        cap.release()


def iter_segments(path: str, every_seconds: float = 0.5, frames_per_segment: int = 6) -> Iterator[Segment]:
    """Group sampled frames into fixed-size Segments."""
    frames: list[object] = []
    stamps: list[float] = []
    for t, frame in sample_frames(path, every_seconds):
        frames.append(frame)
        stamps.append(t)
        if len(frames) == frames_per_segment:
            yield Segment(frames=frames, timestamps=stamps)
            frames, stamps = [], []
