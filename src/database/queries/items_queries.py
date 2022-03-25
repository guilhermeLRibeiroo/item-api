from src.database.db_connection import DBConnector
from src.database.models import Item


def create_item(received_item):
    with DBConnector().conn_session() as session:
        item = Item()

        item.name = received_item

        session.add(item)
        session.flush()

        return item.to_dict()


def update_item(item_id, received_item):
    with DBConnector().conn_session() as session:
        return session.query(Item).filter_by(id=item_id).update({Item.name: received_item.name})
