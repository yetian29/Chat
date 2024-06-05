from dataclasses import dataclass, field
from typing import Set

from src.domain.entities.base import BaseEntity
from src.domain.entities.message import Message
from src.domain.events.message import NewMessageReceivedEvent
from src.domain.value_objects.value import Value


@dataclass
class Chat(BaseEntity):
    title: Value
    messages: Set[Message] = field(default_factory=set, kw_only=True)

    def add_message_to_chat(self, message: Message):
        self.messages.add(message)
        self.push_event(
            NewMessageReceivedEvent(
                chat_id=self.id,
                message_id=message.id,
                message_content=message.content.as_string(),
            )
        )
