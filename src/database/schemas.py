from pydantic import BaseModel


class SUser(BaseModel):
    user_id: int
    tg_id: int
    username: str | None
    name: str | None
    date_of_birth: str | None
    bio: str | None
