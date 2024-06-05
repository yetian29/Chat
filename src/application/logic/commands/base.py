from abc import ABC, abstractmethod
from typing import Generic, TypeVar


class BaseCommand: ...


CT = TypeVar("CT", bound=BaseCommand)
CR = TypeVar("CR")


class CommandHandler(ABC, Generic[CT, CR]):
    @abstractmethod
    def handle(self, command: CT) -> CR: ...
