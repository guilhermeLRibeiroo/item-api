from src.services.models.item_model import ItemRequestModel
from src.database.models import Item

from src.database.queries.generic_queries import generic_get_all, generic_get_by_id, generic_delete_by_id
from src.database.queries.items_queries import create_item, update_item


def get_all():
    return generic_get_all(Item)


def get_by_id(_id):
    return generic_get_by_id(Item, _id)


def delete_by_id(_id):
    return generic_delete_by_id(Item, _id)


def create(received_item: ItemRequestModel):
    return create_item(received_item)


def update(item_id, received_item: ItemRequestModel):
    return update_item(item_id, received_item)