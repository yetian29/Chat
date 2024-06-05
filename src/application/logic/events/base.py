from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.domain.events.base import BaseEvent

ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER")


class EventHandler(ABC, Generic[ET, ER]):

    @abstractmethod
    def handle(self, event: ET) -> ER: ...
