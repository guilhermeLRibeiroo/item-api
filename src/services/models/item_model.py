from pydantic import BaseModel


class ItemBaseModel(BaseModel):
    name: str


class ItemRequestModel(ItemBaseModel):
    pass


class ItemResponseModel(ItemBaseModel):
    id: int
