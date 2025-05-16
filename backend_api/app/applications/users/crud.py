from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from applications.auth.password_handler import PasswordEncrypt
from applications.users.models import User
from applications.users.schemas import BaseFields, RegisterUserFields
from database.sessions_dependencies import get_async_session

async def create_user_in_db(email, name, password, session: AsyncSession):
    hashed_password = await PasswordEncrypt.get_password_hash(password)
    new_user = User(email=email, hashed_password=hashed_password, name=name)
    session.add(new_user)
    await session.commit()