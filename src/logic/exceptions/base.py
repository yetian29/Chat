from src.domain.exceptions.base import BaseAppException


class LogicException(BaseAppException):

    def __init__(self, message: str = "Error occured while processing request"):
        super().__init__(message)
