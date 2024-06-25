from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Generic, TypeVar
from uuid import uuid4


@dataclass
class BaseEvent:
    eid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    registered_at: datetime = field(default_factory=datetime.now, kw_only=True)


ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER", bound=Any)


class BaseEventHandler(ABC, Generic[ET, ER]):
    @abstractmethod
    async def handle(self, event: ET) -> ER: ...
