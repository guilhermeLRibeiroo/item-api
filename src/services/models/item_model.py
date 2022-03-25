from pydantic import BaseModel


class ItemRequestModel(BaseModel):
    name: str
