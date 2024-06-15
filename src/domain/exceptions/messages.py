from src.domain.exceptions.base import BaseAppException


class EmptyMessageException(BaseAppException):
    def __init__(self):
        super().__init__("Message cannot is empty")


class TooLongMessageException(BaseAppException):
    def __init__(self):
        super().__init__("Message cannot be logger than 255 characters")
