from collections import defaultdict
from dataclasses import dataclass, field

from src.logic.commands.base import CT, BaseCommandHandler


@dataclass
class CommandMediator:
    commands_map: dict[CT, list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list)
    )
