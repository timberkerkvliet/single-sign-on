from abc import ABC, abstractmethod
from typing import NewType

Token = NewType('Token', str)


class TokenRegistry(ABC):
    @abstractmethod
    def login(self, user: str, password: str) -> Token:
        ...

    @abstractmethod
    def invalidate_token(self, token: Token) -> None:
        ...

    @abstractmethod
    def is_valid_token(self, token: Token) -> bool:
        ...
