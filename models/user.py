from flask import jsonify

from sql_alchemy import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(70))

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return jsonify(id=self.id, name=self.name,
                       email=self.email, password=self.password)

    @classmethod
    def find_user_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()

        if user:
            return user

        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()
