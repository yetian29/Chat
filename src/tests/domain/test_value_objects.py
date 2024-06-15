import pytest

from src.domain.exceptions.messages import (
    EmptyMessageException,
    TooLongMessageException,
)
from src.domain.value_objects.message import Text


@pytest.mark.parametrize("value", ["", "a" * 256, "hello"])
def test_create_text_success(value):
    if not value:
        with pytest.raises(EmptyMessageException):
            Text(value)
    elif len(value) > 255:
        with pytest.raises(TooLongMessageException):
            Text(value)
    else:
        text = Text(value)
        assert text.as_generic_type() == value
