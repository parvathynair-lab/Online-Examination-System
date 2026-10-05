from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped,mapped_column
from backend.app.database.connection import Base
class Exam(Base):
    __tablename__="exams"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(String(200),nullable=False)
    subject:Mapped[str]=mapped_column(String(100),nullable=False)
    duration:Mapped[int]=mapped_column(Integer,nullable=False)
    tottal_marks:Mapped[int]=mapped_column(Integer,nullable=False)