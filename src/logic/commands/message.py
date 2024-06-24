from dataclasses import dataclass

from src.domain.entities.message import Message
from src.infrastructure.repositories.base import BaseChatRepository
from src.logic.commands.base import BaseCommand, BaseCommandHandler
from src.logic.exceptions.chat import ChatNotFoundException


@dataclass
class CreateMessageCommand(BaseCommand):
    chat_oid: str
    content: str


class CreateMessageCommandHandler(BaseCommandHandler[CreateMessageCommand, Message]):
    def handle(self, command: CreateMessageCommand) -> Message:
        chat_repository: BaseChatRepository
        chat = chat_repository.get_chat_by_oid(oid=command.chat_oid)
        if not chat:
            raise ChatNotFoundException(oid=command.chat_oid)

        return message
