from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Video:
    title: str
    ctr: float
    retention_rate: float
