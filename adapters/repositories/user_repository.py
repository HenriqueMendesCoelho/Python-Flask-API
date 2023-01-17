from adapters.repositories.generic_repository import GenericRepository
from domain.user import UserModel


class UserRepository(GenericRepository):
    def __init__(self):
        super().__init__(UserModel)
