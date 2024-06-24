from dataclasses import dataclass, field
from typing import Optional

from src.domain.entities.chat import Chat
from src.infrastructure.repositories.base import BaseChatRepository
from src.infrastructure.repositories.filters.chat import GetChatsFilters


@dataclass
class MemoryChatRepository(BaseChatRepository):
    _chats: dict[str, Chat] = field(default_factory=dict, kw_only=True)
    _title_index: dict[str, list[Chat]] = field(default_factory=dict, kw_only=True)

    def save_chat(self, chat: Chat) -> None:
        self._chats[chat.oid] = chat
        title = chat.title.as_generic_type()
        if title not in self._title_index:
            self._title_index[title] = []
        self._title_index[title].append(chat)

    def get_chat_by_title(self, title: str) -> Optional[list[Chat]]:
        return self._title_index.get(title, None)

    def get_chat_by_oid(self, oid: str) -> Optional[Chat]:

        return self._chats.get(oid)

    def get_all_chats(self, filters: GetChatsFilters) -> list[Chat]:
        return list(self._chats.values())[filters.offset : filters.limit]
