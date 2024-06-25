from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field

from src.logic.commands.base import CR, CT, BaseCommand, BaseCommandHandler


@dataclass(eq=False)
class CommandMediator(ABC):
    commands_map: dict[CT, list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    @abstractmethod
    def register_command_handlers(
        self, command_type: CT, handlers: Iterable[BaseCommandHandler]
    ) -> None: ...

    @abstractmethod
    def execute(self, commands: Iterable[BaseCommand]) -> list[CR]: ...
