from dataclasses import dataclass

from src.domain.events.base import BaseEvent


@dataclass
class NewChatCreated(BaseEvent):
    chat_id: str
    chat_title: str
