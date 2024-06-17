from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


@dataclass
class BaseCommand(ABC): ...


CT = TypeVar("CT", bound=BaseCommand)  # Command Type
CR = TypeVar("CR", bound=Any)  # Command Result


class BaseCommandHandler(ABC, Generic[CT, CR]):

    @abstractmethod
    def handle(self, command: CT) -> CR: ...
