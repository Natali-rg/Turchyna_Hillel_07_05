import random

from database import engine, Session
from models import Base, Student, Course

# Створення таблиць
Base.metadata.create_all(engine)

session = Session()


# Створення курсів

course_names = [
    "Python",
    "SQL",
    "Java",
    "Testing",
    "DevOps"
]

if session.query(Course).count() == 0:

    for name in course_names:
        session.add(Course(title=name))

    session.commit()



# Створення студентів

student_names = [
    "Ivan", "Petro", "Anna", "Olena", "Andrii",
    "Maksym", "Oksana", "Sofia", "Denys", "Maria",
    "Viktor", "Yulia", "Bohdan", "Kateryna", "Roman",
    "Natalia", "Taras", "Iryna", "Dmytro", "Olha"
]

if session.query(Student).count() == 0:

    courses = session.query(Course).all()

    for name in student_names:

        student = Student(name=name)

        # випадково 1-3 курси
        student.courses = random.sample(
            courses,
            random.randint(1, 3)
        )

        session.add(student)

    session.commit()

print("База заповнена.")


# Додавання нового студента

python_course = session.query(Course).filter_by(title="Python").first()

new_student = Student(name="Natali")

new_student.courses.append(python_course)

session.add(new_student)

session.commit()

print("Новий студент доданий.")


# Запит - студенти певного курсу
course = session.query(Course).filter_by(title="Python").first()

print(f"\nСтуденти курсу {course.title}:")

for student in course.students:
    print(student.name)

#Запит - курси студента
student = session.query(Student).filter_by(name="Natali").first()

print(f"\nКурси студента {student.name}:")

for course in student.courses:
    print(course.title)

#Оновлення
student = session.query(Student).filter_by(name="Natali").first()

student.name = "Natalia"

session.commit()

print("Ім'я оновлено.")

#Видалення
student = session.query(Student).filter_by(name="Natalia").first()

session.delete(student)

session.commit()

print("Студента видалено.")

session.close()