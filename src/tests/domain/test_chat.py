from datetime import datetime

from src.domain.entities.chat import Chat
from src.domain.entities.message import Message
from src.domain.events.chat import NewMessageReceivedEvent
from src.domain.value_objects.message import Text


def test_create_chat_success():
    title = Text(value="Hola")
    chat = Chat(title=title)

    assert chat.title.as_generic_type() == "Hola"
    assert chat.created_at.date() == datetime.today().date()
    assert not chat.messages


def test_add_message_chat_success():
    title = Text(value="Hola")
    chat = Chat(title=title)
    content = Text(value="hi")
    message = Message(content=content)
    chat.add_message_to_chat(message=message)

    assert message in chat.messages


def test_chat_events():

    title = Text(value="Hola")
    chat = Chat(title=title)
    content = Text(value="hi")
    message = Message(content=content)
    chat.add_message_to_chat(message=message)

    events = chat.pull_events()
    first_event = events[0]
    assert len(events) == 1
    assert isinstance(first_event, NewMessageReceivedEvent)
    assert first_event.chat_oid == chat.oid
    assert first_event.message_oid == message.oid
    assert first_event.message_content == message.content.as_generic_type()
