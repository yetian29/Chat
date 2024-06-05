from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.value_objects.value import Value


@dataclass
class Message(BaseEntity):
    content: Value

    def __hash__(self) -> int:
        return hash(self.id)
