from sqlalchemy import Integer,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from backend.app.database.connection import Base
class Attempt(Base):
    __tablename__="attempts"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    exam_id:Mapped[int]=mapped_column(ForeignKey("exams.id"),nullable=False)
    score:Mapped[int]=mapped_column(Integer,default=0,nullable=False)
    total_marks:Mapped[int]=mapped_column(Integer,nullable=False)
