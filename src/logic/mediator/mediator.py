from collections.abc import Iterable
from dataclasses import dataclass

from src.logic.commands.base import CR, CT, BaseCommand, BaseCommandHandler
from src.logic.events.base import ER, ET, BaseEvent, BaseEventHandler
from src.logic.exceptions.mediator import (
    CommandHandlersNotRegisteredException,
    EventHandlersNotRegisteredException,
)
from src.logic.mediator.command import CommandMediator
from src.logic.mediator.event import EventMediator


@dataclass(eq=False)
class Mediator(CommandMediator, EventMediator):
    def register_command_handlers(
        self, command_type: CT, handlers: Iterable[BaseCommandHandler]
    ) -> None:
        self.commands_map[command_type].extend(handlers)

    def register_event_handlers(
        self, event_type: ET, handlers: Iterable[BaseEventHandler]
    ) -> None:
        self.events_map[event_type].extend(handlers)

    def execute(self, commands: Iterable[BaseCommand]) -> list[CR]:
        results = []
        for command in commands:
            command_handlers = self.commands_map.get(type(command))
            if not command_handlers:
                raise CommandHandlersNotRegisteredException(type(command))
            for command_handler in command_handlers:
                result = command_handler.handle(command)
                results.append(result)

        return results

    def public(self, events: Iterable[BaseEvent]) -> list[ER]:
        results = []
        for event in events:
            event_handlers = self.events_map.get(type(event))
            if not event_handlers:
                raise EventHandlersNotRegisteredException(type(event))
            for event_handler in event_handlers:
                result = event_handler.handle(event)
                results.append(result)

        return results
