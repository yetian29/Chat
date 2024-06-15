from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from src.domain.events.base import BaseEvent


@dataclass
class BaseEntity:
    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)

    events: list[BaseEvent] = field(default_factory=list, kw_only=True)

    def register_event(self, event: BaseEvent) -> None:
        self.events.append(event)

    def pull_events(self):
        events = copy(self.events)
        self.events.clear()
        return events
