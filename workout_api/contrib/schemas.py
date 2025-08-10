from pydantic import BaseModel, Field, UUID4
from typing import Annotated

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[str, Field(description='Data de criação')]