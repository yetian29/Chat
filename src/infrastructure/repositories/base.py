from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.chat import Chat
from src.infrastructure.repositories.filters.chat import GetChatsFilters


class BaseChatRepository(ABC):

    @abstractmethod
    def save_chat(self, chat: Chat) -> None: ...

    @abstractmethod
    def get_chat_by_title(self, title: str) -> Optional[Chat]: ...

    def check_chat_exist_by_title(self, title: str) -> bool:
        return bool(self.get_chat_by_title(title))

    @abstractmethod
    def get_chat_by_oid(self, oid: str) -> Optional[Chat]: ...

    @abstractmethod
    def get_all_chats(self, filters: GetChatsFilters) -> list[Chat]
