from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class BaseEvent:
    event_id: UUID = field(default_factory=uuid4, kw_only=True)
