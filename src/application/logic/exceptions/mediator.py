from dataclasses import dataclass

from src.application.logic.exceptions.base import LogicException


@dataclass
class EventHandlerNoPushedException(LogicException):
    event_type: str

    @property
    def message(self):
        return f"Could not find event handler: {self.event_type}"


@dataclass
class CommandHandlerNoPushedException(LogicException):
    command_type: str

    @property
    def message(self):
        return f"Could not find command handler: {self.command_type}"
