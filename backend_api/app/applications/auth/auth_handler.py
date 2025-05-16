from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from settings import settings


class AuthHandler:
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM

    async def get_login_token_pairs(self, data: OAuth2PasswordRequestForm, session: AsyncSession):
        user_email = data.username
        user_password = data.password

auth_handler = AuthHandler()
