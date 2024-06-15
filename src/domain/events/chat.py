from dataclasses import dataclass
from typing import ClassVar

from src.domain.events.base import BaseEvent


@dataclass
class NewMessageReceivedEvent(BaseEvent):
    event_title: ClassVar[str] = "New Message Received"  # Direct access from the class
    chat_oid: str
    message_oid: str
    message_content: str
