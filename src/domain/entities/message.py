from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.value_objects.message import Text


@dataclass(eq=False)
class Message(BaseEntity):
    content: Text
