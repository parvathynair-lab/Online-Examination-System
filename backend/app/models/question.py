from sqlalchemy import String,Integer,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from backend.app.database.connection import Base
class Question(Base):
    __tablename__="questions"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    exam_id:Mapped[int]=mapped_column(ForeignKey("exams.id"),nullable=False)
    question_text:Mapped[str]=mapped_column(String(500),nullable=False)
    option_a:Mapped[str]=mapped_column(String(255),nullable=False)
    option_b:Mapped[str]=mapped_column(String(255),nullable=False)
    option_c:Mapped[str]=mapped_column(String(255),nullable=False)
    option_d:Mapped[str]=mapped_column(String(255),nullable=False)
    option_e:Mapped[str]=mapped_column(String(255),nullable=False)
    correct_answer:Mapped[str]=mapped_column(String(1),nullable=False)
    marks:Mapped[int]=mapped_column(Integer,default=1,nullable=False)
