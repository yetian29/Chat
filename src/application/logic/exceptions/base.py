from src.domain.exceptions.base import BaseApplicationException


class LogicException(BaseApplicationException):
    @property
    def message(self):
        return "An error occured while processing the request"
