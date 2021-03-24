from typing import List

from flask_restful import reqparse
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from models.user import User


def get_args_parser(args: List[dict]) -> reqparse.RequestParser:
    """
    This function accepts list of arguments
    and returns parser
    """
    parser = reqparse.RequestParser()
    for arg in args:
        parser.add_argument(**arg)
    return parser


def get_user(name: str, session: Session) -> User:
    """ Gets the user by name """

    try:
        user = session.query(User).filter(User.name == name).one()
        return user
    except NoResultFound:
        pass

