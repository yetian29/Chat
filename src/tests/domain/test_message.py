from datetime import datetime

from src.domain.entities.message import Message
from src.domain.value_objects.message import Text


def test_create_message_success():
    value = "hello"
    content = Text(value=value)
    message = Message(content=content)
    assert message.content.as_generic_type() == value
    assert message.created_at.date() == datetime.today().date()
