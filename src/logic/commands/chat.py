from dataclasses import dataclass
from typing import Iterable

from src.domain.entities.chat import Chat
from src.domain.value_objects.message import Text
from src.infrastructure.repositories.base import BaseChatRepository
from src.infrastructure.repositories.filters.chat import GetChatsFilters
from src.logic.command.base import BaseCommand, BaseCommandHandler
from src.logic.exceptions.chat import (
    ChatNotFoundException,
    ChatWithTitleAlreadyExistException,
)


@dataclass
class CreateChatCommand(BaseCommand):
    title: str


class CreateChatCommandHandler(BaseCommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRepository

    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chat_repository.check_chat_exist_by_title(title=command.title):
            raise ChatWithTitleAlreadyExistException(title=command.title)

        chat = Chat.create_chat(title=Text(value=command.title))
        await self.chat_repository.save_chat(chat)
        return chat


@dataclass
class GetChatCommand(BaseCommand):
    oid: str


class GetChatCommandHandler(BaseCommandHandler[GetChatCommand, Chat]):
    chat_repository: BaseChatRepository

    def hanlde(self, command: GetChatCommand) -> Chat:
        chat = self.chat_repository.get_chat_by_oid(oid=command.oid)
        if not chat:
            raise ChatNotFoundException(oid=command.oid)
        return chat


@dataclass
class GetAllChatsCommand(BaseCommand):
    filters: GetChatsFilters


class GetAllChatsCommandHandler(
    BaseCommandHandler[GetAllChatsCommand, tuple[Iterable[Chat], int]]
):

    chat_repository: BaseChatRepository

    def handle(self, command: GetAllChatsCommand) -> tuple[list[Chat], int]:
        chats, count = self.chat_repository.get_all_chats(filters=command.filters)
        return chats, count


@dataclass
class DeleteChatCommand(BaseCommand):
    oid: str


class DeleteChatCommandHandler(BaseCommandHandler[DeleteChatCommand, Chat]):
    chat_repository: BaseChatRepository

    def handle(self, command: DeleteChatCommand) -> Chat:
        chat = self.chat_repository.get_chat_by_oid(oid=command.oid)
        if not chat:
            raise ChatNotFoundException(oid=command.oid)
        chat.delete_chat()
        return chat
