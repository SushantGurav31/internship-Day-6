# from sqlalchemy import Column, Integer, String, Text, Date
# from database import Base


# class Projects(Base):
#     __tablename__ = "projects"

#     project_id = Column(Integer, primary_key=True, index=True)
#     project_name = Column(String(100), nullable=False)
#     description = Column(Text, nullable=True)
#     start_date = Column(Date, nullable=False)
#     end_date = Column(Date, nullable=False)
#     status = Column(String(100), nullable=False)

from sqlalchemy import Column, Integer, String, Text, Date
from database import Base


class Projects(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String(100), nullable=False)