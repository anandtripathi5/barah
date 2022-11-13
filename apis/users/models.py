from enum import Enum

from extensions import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ChoiceType, PasswordType


class PermissionEnum(Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    email = Column(String(256), unique=True)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    permission = Column(ChoiceType(PermissionEnum, impl=String(256)),
                        default=PermissionEnum.user)
