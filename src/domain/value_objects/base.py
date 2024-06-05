from abc import ABC, abstractmethod


class BaseValueObjects(ABC):

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self) -> None: ...

    @abstractmethod
    def as_string(self) -> str: ...
