from dataclasses import dataclass
from typing import Any

from src.domain.exceptions.messages import (
    EmptyContentException,
    TooLongContentException,
)
from src.domain.value_objects.base import BaseValueObjects


@dataclass
class Value(BaseValueObjects):
    value: Any

    def validate(self):
        if not self.value:
            raise EmptyContentException()

        if len(str(self.value)) > 255:
            raise TooLongContentException(self.value)

    def as_string(self) -> str:
        return str(self.value)
