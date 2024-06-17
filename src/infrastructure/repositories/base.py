from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.chat import Chat


class BaseChatRepository(ABC):
    @abstractmethod
    def get_chat_by_title(self, title: str) -> Optional[Chat]: ...

    def check_chat_exist_by_title(self, title: str) -> bool:
        return bool(self.get_chat_by_title(title))
