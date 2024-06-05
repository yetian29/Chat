from dataclasses import dataclass

from src.application.logic.exceptions.base import LogicException


@dataclass
class ChatWithTitleAlreadyExistException(LogicException):
    title: str

    @property
    def message(self):
        return f"Chat with Title: {self.title} Already Exist"
