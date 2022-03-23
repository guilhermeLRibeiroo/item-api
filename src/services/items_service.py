from src.services.models.item_model import ItemRequestModel
from src.database.models import Item

from src.database.queries import generic_get_all, generic_get_by_id, generic_delete_by_id


def get_all():
    return generic_get_all(Item)


def get_by_id(_id: int):
    return generic_get_by_id(id)


def delete_by_id(_id: int):
    try:
        generic_delete_by_id(_id)
        return True
    except:
        return False
