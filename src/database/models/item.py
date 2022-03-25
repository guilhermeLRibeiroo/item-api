from sqlalchemy import Column, String
from src.database.models.base import BaseModel


class Item(BaseModel):
    __tablename__ = 'items'

    name = Column(String)

    def __repr__(self):
        return f'<Item id={self.id} name={self.name} />'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
