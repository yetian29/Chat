from dataclasses import dataclass

from src.application.logic.commands.base import BaseCommand, CommandHandler
from src.application.logic.exceptions.messages import ChatWithTitleAlreadyExistException
from src.domain.entities.messages import Chat
from src.domain.value_objects.messages import Value


@dataclass
class CreateChatCommand(BaseCommand):
    title: str


class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRespository

    def handle(self, command: CreateChatCommand) -> Chat:
        if self.chat_repository.check_chat_exist_by_title(command.title):
            raise ChatWithTitleAlreadyExistException(command.title)
        title = Value(value=command.title)
        chat = Chat(title=title)
        return chat
