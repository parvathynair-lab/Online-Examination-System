from sqlalchemy import String,Integer,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from backend.app.database.connection import Base
class Answer(Base):
    __tablename__="answers"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    attempt_id:Mapped[int]=mapped_column(ForeignKey("attempts.id"),nullable=False)
    question_id:Mapped[int]=mapped_column(ForeignKey("questions.id"),nullable=False)
    selected_answer:Mapped[str]=mapped_column(String(1),nullable=False)
    is_correct:Mapped[int]=mapped_column(Integer,nullable=False)