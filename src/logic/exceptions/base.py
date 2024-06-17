from src.domain.exceptions.base import BaseAppException


class LogicException(BaseAppException):

    def __init__(self, message: str = "Error occured while processing request"):
        self.message = message
        super().__init__(message)
