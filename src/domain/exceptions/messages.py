from dataclasses import dataclass

from src.domain.exceptions.base import BaseApplicationException


class EmptyContentException(BaseApplicationException):
    @property
    def message(self):
        return "No Content"


@dataclass
class TooLongContentException(BaseApplicationException):
    value: str

    @property
    def message(self):
        return f"The Content is too long compared to regulation, {self.value[:255]}..."
