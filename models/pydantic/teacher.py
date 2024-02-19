from pydantic import BaseModel


class Teacher(BaseModel):
    full_name: str
    telegram_id: int
    is_admin: bool
    assigned_disciplines: list[str]
    assigned_groups: list[str]
