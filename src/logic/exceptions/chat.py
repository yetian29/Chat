from src.logic.exceptions.base import LogicException


class ChatWithTitleAlreadyExistException(LogicException):
    def __init__(self, title: str):
        super().__init__(f"Chat with title <{title}> already exist")


class ChatNotFoundException(LogicException):
    def __init__(self, oid: str):
        super().__init__(f"Chat With <{oid}> not found")
