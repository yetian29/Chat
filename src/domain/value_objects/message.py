from dataclasses import dataclass

from src.domain.exceptions.messages import (
    EmptyMessageException,
    TooLongMessageException,
)
from src.domain.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self) -> None:
        if not self.value:
            raise EmptyMessageException()
        if len(self.value) > 255:
            raise TooLongMessageException()

    def as_generic_type(self) -> str:
        return str(self.value)
