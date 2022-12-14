from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends
from jose import (
    JWTError,
    jwt,
)
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from ..database import get_session
from ..settings import settings
from fastapi.security import OAuth2PasswordBearer

from src import models, tables

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')


def get_current_user(token: str = Depends(oauth_scheme)) -> models.User:
    return AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> models.User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authenticate': 'Bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception

        user_data = payload.get('user')

        try:
            user = models.User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: tables.User) -> models.Token:
        user_data = models.User.from_orm(user)

        now = datetime.utcnow()
        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(seconds=settings.jwt_expiration),
            "user": user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return models.Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: models.UserCreate) -> models.Token:
        self.ensure_username_or_email_in_db(username=user_data.username, email=user_data.email)
        user = tables.User(
            email=user_data.email,
            username=user_data.username,
            phone_number=user_data.phone_number,
            password_hash=self.hash_password(user_data.password)
        )
        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> models.Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={
                'WWW-Authenticate': 'Bearer'
            },
        )

        user = (
            self.session
            .query(tables.User)
            .filter(tables.User.username == username)
            .first()
        )

        if not user:
            raise exception
        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)

    def ensure_username_or_email_in_db(self, username: str, email: str):
        user_username = (
            self.session
            .query(tables.User)
            .filter(tables.User.username == username)
            .first()
        )
        user_email = (
            self.session
            .query(tables.User)
            .filter(tables.User.email == email)
            .first()
        )
        if user_email and user_username:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'Username {username} and e-mail {email} already exists',
            )
        if user_username:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'Username {username} already exists',
            )
        if user_email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'e-mail {email} already exists',
            )
