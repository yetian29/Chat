from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar("T", bound=Any)


class BaseValueObject(ABC, Generic[T]):
    value: T

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self) -> None: ...

    @abstractmethod
    def as_generic_type(self) -> T: ...
