from dataclasses import dataclass, field
from typing import Optional

from src.domain.entities.chat import Chat
from src.infrastructure.repositories.base import BaseChatRepository
from src.infrastructure.repositories.filters.chat import GetChatsFilters


@dataclass
class MemoryChatRepository(BaseChatRepository):
    _chats: dict[int, Chat] = field(default_factory=dict, kw_only=True)

    def save_chat(self, chat: Chat) -> None:
        oid = chat.oid
        oid_hash = hash(oid)
        self._chats[oid_hash] = chat

    def get_chat_by_title(self, title: str) -> Optional[Chat]:
        for chat in self._chats.values():
            if chat.title.as_generic_type() == title:
                return chat

        return None

    def get_chat_by_oid(self, oid: str) -> Optional[Chat]:
        oid_hash = hash(oid)

        return self._chats.get(oid_hash)

    def get_all_chats(self, filters: GetChatsFilters) -> list[Chat]:
        return list(self._chats.values())[filters.offset : filters.limit]
