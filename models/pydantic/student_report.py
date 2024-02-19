from pydantic import BaseModel


class StudentReport(BaseModel):
    full_name: str = ''
    points: float = 0
    lab_complited: int = 0
    deadlines_fails: int = 0
    task_complited: int = 0   
    task_ratio: int = 0
