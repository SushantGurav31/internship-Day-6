# from pydantic import BaseModel
# from datetime import date
# from typing import Optional


# class ProjectBase(BaseModel):
#     project_name: str
#     description: Optional[str] = None
#     start_date: date
#     end_date: date
#     status: str


# class ProjectCreate(ProjectBase):
#     pass


# class ProjectUpdate(BaseModel):
#     project_name: Optional[str] = None
#     description: Optional[str] = None
#     start_date: Optional[date] = None
#     end_date: Optional[date] = None
#     status: Optional[str] = None


# class ProjectResponse(ProjectBase):
#     project_id: int

#     class Config:
#         from_attributes = True


from pydantic import BaseModel
from datetime import date
from typing import Optional


class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str] = None
    start_date: date
    end_date: date
    status: str


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None


class ProjectResponse(ProjectBase):
    project_id: int

    class Config:
        from_attributes = True