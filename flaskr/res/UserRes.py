from datetime import datetime

from flask import request
from flask_restful import Resource

from config import db
from models.user import User
from schemas.user import UserSchema
from utils import get_args_parser

user_schema = UserSchema(many=False)
parser = get_args_parser([
    {'name': "num_mark_tasks", 'type': int, 'required': True,
     'help': 'number of mark tasks the user has'},
    {'name': "password", 'type': str, 'required': False,
     'help': 'unprocessed password of the user'},
    {'name': "name", 'type': str, 'required': True,
     'help': 'name of the user'}
])


class UserResource(Resource):
    """Resource to handle CRUD operations for users table"""

    @staticmethod
    def get(user_id: int):
        """
        Returns single user
        """

        if not user_id:
            return {'status': 'failed', 'message': "Empty ID field"}, 404

        user = User.query.filter(User.user_id == user_id).one_or_none()
        if not user:
            return {'status': 'failed', 'message': "User not found"}, 404

        return {'data': user_schema.dump(user)}, 200

    @staticmethod
    def post(user_id: int):
        """
        Creates new user
        """

        request.get_json(force=True)
        data = parser.parse_args(strict=True)
        if not data:
            return {'status': 'failed', 'message': 'No input data provided'}, 204

        user = User.query.filter_by(user_id=user_id).one_or_none()
        if user:
            return {'status': 'failed', 'message': 'User already exists'}, 400

        data.update({'user_id': user_id, 'last_activity_ds': datetime.now(),
                     'registration_date': datetime.now()})
        user = User(**data)
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user)

        return {"status": 'success', 'data': result}, 201

    @staticmethod
    def put(user_id: int):
        """
        Updates the user
        Possible fields for update:
            'num_mark_tasks': int,
            'password': str,
            'name': str,
            'last_name': str
        """

        request.get_json(force=True)
        data = parser.parse_args(strict=True)
        if not data:
            return {'status': 'failed', 'message': 'No input data provided'}, 204

        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return {'status': 'failed', 'message': 'User does not exist'}, 204

        for k, v in data.items():
            user.__setattr__(k, v)
        db.session.commit()

        result = user_schema.dump(user)
        return {"status": 'success', 'data': result}, 202

    @staticmethod
    def delete(user_id):
        """
        Deletes single user
        """

        user = User.query.filter_by(user_id=user_id).one_or_none()
        if not user:
            return {'status': 'failed',
                    'message': 'User does not exist'}, 204
        User.query.filter_by(user_id=user_id).delete()
        db.session.commit()

        result = user_schema.dump(user)
        return {"status": 'success', 'data': result}, 202
