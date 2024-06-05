from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import UUID, uuid4

from src.domain.events.base import BaseEvent


@dataclass
class BaseEntity:
    id: UUID = field(default_factory=uuid4, kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    _events: List[BaseEvent] = field(default_factory=list, kw_only=True)

    def push_event(self, event: BaseEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> List[BaseEvent]:
        registered_events = copy(self._events)
        self._events.clear()
        return registered_events
