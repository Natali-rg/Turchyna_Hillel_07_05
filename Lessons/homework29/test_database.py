import allure

from sqlalchemy import text

from database import engine, Session
from models import Base, Student


def setup_module():
    """
    Create tables before running tests.
    """
    Base.metadata.create_all(engine)


@allure.feature("Database")
@allure.story("Database connection")
@allure.title("Check database connection")
def test_database_connection():

    with allure.step("Connect to PostgreSQL"):
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))

    with allure.step("Check database response"):
        assert result.scalar() == 1


@allure.feature("Database")
@allure.story("Student management")
@allure.title("Insert a new student")
def test_insert_student():

    with allure.step("Create a new student"):
        session = Session()
        student = Student(name="Test Student")

    try:
        with allure.step("Save student to database"):
            session.add(student)
            session.commit()

        with allure.step("Check that student was created"):
            saved_student = (
                session.query(Student)
                .filter_by(name="Test Student")
                .first()
            )

            assert saved_student is not None
            assert saved_student.name == "Test Student"
            assert saved_student.id is not None

    finally:
        session.close()


@allure.feature("Database")
@allure.story("Student management")
@allure.title("Select student from database")
def test_select_student():

    session = Session()

    try:
        with allure.step("Find Test Student in database"):
            student = (
                session.query(Student)
                .filter_by(name="Test Student")
                .first()
            )

        with allure.step("Check selected student"):
            assert student is not None
            assert student.name == "Test Student"

    finally:
        session.close()


@allure.feature("Database")
@allure.story("Student management")
@allure.title("Update student")
def test_update_student():

    session = Session()

    try:
        with allure.step("Find Test Student"):
            student = (
                session.query(Student)
                .filter_by(name="Test Student")
                .first()
            )

            assert student is not None

        with allure.step("Update student name"):
            student.name = "Updated Student"
            session.commit()

        with allure.step("Check updated student"):
            updated_student = (
                session.query(Student)
                .filter_by(name="Updated Student")
                .first()
            )

            assert updated_student is not None
            assert updated_student.name == "Updated Student"

    finally:
        session.close()


@allure.feature("Database")
@allure.story("Student management")
@allure.title("Delete student")
def test_delete_student():

    session = Session()

    try:
        with allure.step("Find Updated Student"):
            student = (
                session.query(Student)
                .filter_by(name="Updated Student")
                .first()
            )

            assert student is not None

        with allure.step("Delete student"):
            session.delete(student)
            session.commit()

        with allure.step("Check that student was deleted"):
            deleted_student = (
                session.query(Student)
                .filter_by(name="Updated Student")
                .first()
            )

            assert deleted_student is None

    finally:
        session.close()