from dataclasses import dataclass, field
from typing import Optional

from src.domain.entities.chat import Chat
from src.infrastructure.repositories.base import BaseChatRepository


@dataclass
class MemoryChatRepository(BaseChatRepository):
    _chats: list[Chat] = field(default_factory=list, kw_only=True)

    def get_chat_by_title(self, title: str) -> Optional[Chat]:
        for chat in self._chats:
            if chat.title.as_generic_type() == title:
                return chat

        return None
