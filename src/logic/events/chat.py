from dataclasses import dataclass
from typing import ClassVar

from src.logic.events.base import BaseEvent


@dataclass
class NewChatCreatedEvent(BaseEvent):
    event_title: ClassVar[str] = "New Chat Created"
    chat_oid: str
    title: str


@dataclass
class ChatDeletedEvent(BaseEvent):
    event_title: ClassVar[str] = "Chat was deleted"
    chat_oid: str
    title: str


@dataclass
class NewMessageReceivedEvent(BaseEvent):
    event_title: ClassVar[str] = "New Message Received"  # Direct access from the class
    chat_oid: str
    message_oid: str
    message_content: str
