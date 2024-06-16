from dataclasses import dataclass, field

from src.domain.entities.base import BaseEntity
from src.domain.entities.message import Message
from src.domain.events.chat import (
    ChatDeletedEvent,
    NewChatCreatedEvent,
    NewMessageReceivedEvent,
)
from src.domain.value_objects.message import Text


@dataclass(eq=False)
class Chat(BaseEntity):
    title: Text
    messages: list[Message] = field(default_factory=list, kw_only=True)
    is_deleted: bool = field(default=False, kw_only=True)

    def add_message_to_chat(self, message: Message) -> None:
        self.messages.append(message)
        self.register_event(
            NewMessageReceivedEvent(
                chat_oid=self.oid,
                message_oid=message.oid,
                message_content=message.content.as_generic_type(),
            )
        )

    @classmethod
    def create_chat(cls, title: Text) -> "Chat":
        new_chat = cls(title=title)
        new_chat.register_event(
            NewChatCreatedEvent(chat_oid=new_chat.oid, title=title.as_generic_type())
        )
        return new_chat

    def delete_chat(self) -> None:
        self.is_deleted = True
        self.register_event(
            ChatDeletedEvent(chat_oid=self.oid, title=self.title.as_generic_type())
        )
