from datetime import datetime

import pytest

from src.domain.entities.chat import Chat
from src.domain.entities.message import Message
from src.domain.events.message import NewMessageReceivedEvent
from src.domain.exceptions.messages import (
    EmptyContentException,
    TooLongContentException,
)
from src.domain.value_objects.value import Value


@pytest.mark.parametrize("value", ["", "a" * 256])
def test_create_value(value):
    if not value:
        with pytest.raises(EmptyContentException):
            Value(value)
    else:
        with pytest.raises(TooLongContentException):
            Value(value)


@pytest.mark.parametrize("value", ["hello", 12345])
def test_create_message(value):
    content = Value(value)
    message = Message(content)
    assert message.content.as_string() == content.as_string()
    assert message.created_at.date() == datetime.now().date()


@pytest.mark.parametrize("value", ["hi"])
def test_create_chat(value):
    title = Value(value)
    chat = Chat(title)
    assert chat.title.as_string() == title.as_string()
    assert chat.created_at.date() == datetime.now().date()
    assert not chat.messages


@pytest.mark.parametrize("value", ["hi"])
def test_add_message_to_chat(value):

    title = Value(value)
    chat = Chat(title)
    content = Value(value)
    message = Message(content)
    chat.add_message_to_chat(message)
    assert message in chat.messages


@pytest.mark.parametrize("value", ["hi"])
def test_new_message_received_event(value):
    title = Value(value)
    chat = Chat(title)
    content = Value(value)
    message = Message(content)
    chat.add_message_to_chat(message)
    events = chat.pull_events()
    assert len(events) == 1
    new_event = events[0]
    assert isinstance(new_event, NewMessageReceivedEvent), new_event
    assert new_event.chat_id == chat.id
    assert new_event.message_id == message.id
    assert new_event.message_content == message.content.as_string()
