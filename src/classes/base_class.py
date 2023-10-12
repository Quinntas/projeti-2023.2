from pydantic import BaseModel


class BaseClass(BaseModel):
    class Config:
        arbitrary_types_allowed = True
