from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Таблиця зв'язку багато-до-багатьох
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )

    def __repr__(self):
        return f"Course(id={self.id}, title='{self.title}')"