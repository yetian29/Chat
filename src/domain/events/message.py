from dataclasses import dataclass

from src.domain.events.base import BaseEvent


@dataclass
class NewMessageReceivedEvent(BaseEvent):
    chat_id: str
    message_id: str
    message_content: str
