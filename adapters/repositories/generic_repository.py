from adapters.sql_alchemy import db
from domain.user import UserModel


class GenericRepository:

    def __init__(self, entity: object):
        self.entity = entity

    def find_by_id(self, id):
        user = db.session.query(self.entity).filter_by(id=id).first()

        if user:
            return user
        return None

    def save_and_flush(self, user: UserModel):
        db.session.add(user)
        db.session.commit()

    def list(self):
        users = db.session.query(self.entity).all()

        if len(users) > 0:
            return users

        return None

    def delete_by_id(self, id):
        user = db.session.query(self.entity).filter_by(id=id).first()

        if not user:
            return

        db.session.delete(user)
        db.session.commit()
