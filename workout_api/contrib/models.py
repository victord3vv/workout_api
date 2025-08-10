from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid
from datetime import datetime

class BaseModel(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid.uuid4, nullable=False, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)