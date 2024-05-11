from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from sqlalchemy import SmallInteger, BigInteger, Text


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, index=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(Text, nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    date_of_birth: Mapped[int] = mapped_column(Text, nullable=True)
    bio: Mapped[str | None] = mapped_column(Text)
