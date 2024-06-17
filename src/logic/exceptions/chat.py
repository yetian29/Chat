from src.logic.exceptions.base import LogicException


class ChatWithTitleAlreadyExistException(LogicException):
    def __init__(self, title: str):
        super().__init__(f"Chat with title <{title}> already exist")
