from dataclasses import dataclass

from src.domain.entities.chat import Chat
from src.domain.value_objects.message import Text
from src.logic.command.base import BaseCommand, BaseCommandHandler


@dataclass
class CreateChatCommand(BaseCommand):
    title: str


class CreateChatCommandHandler(BaseCommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRepository

    def handle(self, command: CreateChatCommand) -> Chat:
        if chat_repository.check_chat_exist_by_title:
            raise ChatWithTitleAlreadyExistException(title=command.title)

        chat = Chat.create_chat(title=Text(value=command.title))
        return chat
