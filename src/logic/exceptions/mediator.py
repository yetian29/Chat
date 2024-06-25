from src.logic.exceptions.base import LogicException


class CommandHandlersNotRegisteredException(LogicException):
    def __init__(self, command_type: type):
        super().__init__(f"Cound not command handlers for {command_type}")


class EventHandlersNotRegisteredException(LogicException):
    def __init__(self, event_type: type):
        super().__init__(f"Cound not event handlers for {event_type}")
