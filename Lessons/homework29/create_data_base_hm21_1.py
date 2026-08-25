from database import engine, Session
from models import Base, Student, Course

# Створення таблиць
Base.metadata.create_all(engine)

session = Session()

try:
    # Створення курсів
    course_names = [
        "Python",
        "SQL",
        "Java",
        "Testing",
        "DevOps"
    ]

    for course_name in course_names:
        existing_course = (
            session.query(Course)
            .filter_by(title=course_name)
            .first()
        )

        if not existing_course:
            session.add(Course(title=course_name))

    session.commit()

    # Створення студентів
    student_names = [
        "Ivan",
        "Petro",
        "Anna",
        "Olena",
        "Andrii",
        "Maksym",
        "Oksana",
        "Sofia",
        "Denys",
        "Maria"
    ]

    courses = session.query(Course).all()

    for student_name in student_names:
        existing_student = (
            session.query(Student)
            .filter_by(name=student_name)
            .first()
        )

        if not existing_student:
            student = Student(name=student_name)
            student.courses.append(courses[0])
            session.add(student)

    session.commit()

    print("База даних успішно створена та заповнена.")

finally:
    session.close()