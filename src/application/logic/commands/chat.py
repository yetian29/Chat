from dataclasses import dataclass

from src.application.logic.commands.base import BaseCommand, CommandHandler
from src.application.logic.exceptions.chat import ChatWithTitleAlreadyExistException
from src.domain.entities.chat import Chat
from src.domain.value_objects.value import Value
from src.infrastructure.repositories.chat import BaseChatRespository


@dataclass
class CreateChatCommand(BaseCommand):
    title: str


@dataclass
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRespository

    def handle(self, command: CreateChatCommand) -> Chat:
        if self.chat_repository.check_chat_exist_by_title(command.title):
            raise ChatWithTitleAlreadyExistException(command.title)
        title = Value(value=command.title)
        chat = Chat.create_chat(title=title)
        return chat
