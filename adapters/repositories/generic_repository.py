from adapters.sql_alchemy import db


class GenericRepository:

    entity: object = NotImplemented

    def __init__(self, entity: object):
        self.entity = entity

    def find_by_id(self, id):
        entity = db.session.query(self.entity).filter_by(id=id).first()

        if entity:
            return entity
        return None

    def list(self):
        entitys = db.session.query(self.entity).all()

        if len(entitys) > 0:
            return entitys

        return None

    def save_and_flush(self, entity):
        db.session.add(entity)
        db.session.commit()

    def delete_by_id(self, id):
        entity = db.session.query(self.entity).filter_by(id=id).first()

        if not entity:
            return

        db.session.delete(entity)
        db.session.commit()
