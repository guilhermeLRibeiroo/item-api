from src.database.db_connection import DBConnector


def generic_get_all(db_model):
    with DBConnector().conn_session() as session:
        db_models = session.query(db_model).all()
        return [db_model.to_dict() for db_model in db_models]


def generic_get_by_id(db_model, object_id):
    with DBConnector().conn_session() as session:
        db_object = session.query(db_model).filter_by(id=object_id).first()
        return db_object.to_dict()


def generic_delete_by_id(db_model, object_id):
    with DBConnector().conn_session() as session:
        session.query(db_model).filter_by(id=object_id).delete()
