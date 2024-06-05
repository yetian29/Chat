from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict

from src.application.logic.commands.base import CR, CT, CommandHandler
from src.application.logic.events.base import ER, ET, EventHandler
from src.application.logic.exceptions.mediator import (
    CommandHandlerNoPushedException,
    EventHandlerNoPushedException,
)


@dataclass
class Mediator:
    events_map: Dict[ET, EventHandler] = field(
        default_factory=defaultdict(list), kw_only=True
    )
    commands_map: Dict[CT, CommandHandler] = field(
        default_factory=defaultdict(list), kw_only=True
    )

    def push_event(self, event_type: ET, event_handler: EventHandler[ET, ER]):
        self.events_map[event_type] = event_handler

    def push_command(self, command_type: CT, command_handler: CommandHandler[CT, CR]):
        self.commands_map[command_type] = command_handler

    def handle_event(self, event_type: ET) -> ER:
        event_handler = self.events_map[event_type]
        if event_handler:
            return event_handler.handle(event_type)
        raise EventHandlerNoPushedException(event_type)

    def handle_command(self, command_type: CT) -> CR:
        command_handler = self.commands_map[command_type]
        if command_handler:
            return command_handler.handle(command_type)
        raise CommandHandlerNoPushedException(command_type)
