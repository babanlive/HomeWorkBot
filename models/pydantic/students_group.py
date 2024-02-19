from pydantic import BaseModel


class StudentsGroup(BaseModel):
    group_name: str
    discilpline_short_name: list[str]
    students: list[str]
