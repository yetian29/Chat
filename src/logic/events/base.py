from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class BaseEvent:
    eid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    registered_at: datetime = field(default_factory=datetime.now, kw_only=True)
