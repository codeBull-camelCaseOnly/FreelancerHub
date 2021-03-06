from dataclasses import dataclass

from lib.model import Model


@dataclass
class User_auth(Model):
    user_id: int
    token: str
