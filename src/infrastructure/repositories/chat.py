from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Set

from src.domain.entities.chat import Chat


class BaseChatRespository(ABC):
    @abstractmethod
    def check_chat_exist_by_title(self, title: str) -> bool: ...


@dataclass
class MemoryChatRepository(BaseChatRespository):
    _saved_chats: Set[Chat] = field(default_factory=set, kw_only=True)

    def check_chat_exist_by_title(self, title: str) -> bool:
        for chat in self._saved_chats:
            if chat.title.as_string() == title:
                return True
        return False
