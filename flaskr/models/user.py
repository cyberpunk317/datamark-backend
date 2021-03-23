from sqlalchemy.orm import relationship

from config import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registration_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=True)
    name = db.Column(db.String(15), nullable=True)
    password = db.Column(db.String(128), nullable=True)
    num_mark_tasks = db.Column(db.Integer, nullable=True)
    last_activity_ds = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=True)

    def __repr__(self):
        return f'<User: {self.name}>'
