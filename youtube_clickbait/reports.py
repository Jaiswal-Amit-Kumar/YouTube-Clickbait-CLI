from __future__ import annotations

from abc import ABC, abstractmethod

from .models import Video


class BaseReport(ABC):
    @abstractmethod
    def build(self, videos: list[Video]) -> list[dict[str, object]]:
        raise NotImplementedError


class ClickbaitReport(BaseReport):
    def build(self, videos: list[Video]) -> list[dict[str, object]]:
        filtered = [
            video
            for video in videos
            if video.ctr > 15 and video.retention_rate < 40
        ]
        filtered.sort(key=lambda video: video.ctr, reverse=True)

        return [
            {
                "title": video.title,
                "ctr": video.ctr,
                "retention_rate": video.retention_rate,
            }
            for video in filtered
        ]


REPORTS: dict[str, type[BaseReport]] = {
    "clickbait": ClickbaitReport,
}
