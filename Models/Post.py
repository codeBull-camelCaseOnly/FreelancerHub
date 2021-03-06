import typing
from dataclasses import dataclass

from Models import User
from lib.model import Model


@dataclass
class Post(Model):
    user_id: int
    title: str
    content: typing.AnyStr
    allow_comments: int
    public_visibility: int
    tags: str

    def getUserName(self):
        return User.query().select().where('id', self.user_id).getOne().name