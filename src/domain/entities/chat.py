from dataclasses import dataclass, field

from src.domain.entities.base import BaseEntity
from src.domain.entities.message import Message
from src.domain.events.chat import NewMessageReceivedEvent
from src.domain.value_objects.message import Text


@dataclass
class Chat(BaseEntity):
    title: Text
    messages: list[Message] = field(default_factory=list, kw_only=True)

    def add_message_to_chat(self, message: Message) -> None:
        self.messages.append(message)
        self.register_event(
            NewMessageReceivedEvent(
                chat_oid=self.oid,
                message_oid=message.oid,
                message_content=message.content.as_generic_type(),
            )
        )
