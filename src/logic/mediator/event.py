from abc import abstractmethod
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

from src.logic.events.base import ER, ET, BaseEvent, BaseEventHandler


@dataclass(eq=False)
class EventMediator:
    events_map: dict[ET, list[BaseEventHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    @abstractmethod
    def register_event_handlers(
        self, event_type: ET, handlers: Iterable[BaseEventHandler]
    ) -> None: ...

    @abstractmethod
    def public(self, events: Iterable[BaseEvent]) -> list[ER]: ...
