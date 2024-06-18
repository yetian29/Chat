from dataclasses import dataclass, field
from typing import Optional

from src.domain.entities.chat import Chat
from src.infrastructure.repositories.base import BaseChatRepository


@dataclass
class MemoryChatRepository(BaseChatRepository):
    _chats: set[Chat] = field(default_factory=set, kw_only=True)
    title_index: dict[str, Chat] = field(default_factory=dict, kw_only=True)

    def get_chat_by_title(self, title: str) -> Optional[Chat]:
        return self.title_index.get(title)  # return chat or None
