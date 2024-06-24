from collections import defaultdict
from dataclasses import dataclass, field

from src.logic.events.base import ET, BaseEvent


@dataclass
class EventMediator:
    events_map: dict[ET, list[BaseEvent]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )
