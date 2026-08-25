from sqlalchemy import text

from database import engine, Session
from models import Base, Student, Course


def setup_module():
    """
    Створюємо таблиці перед запуском тестів.
    """
    Base.metadata.create_all(engine)


def test_database_connection():
    """
    Перевірка підключення до PostgreSQL.
    """
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_insert_student():
    """
    Перевірка вставки нового студента.
    """
    session = Session()

    try:
        student = Student(name="Test Student")
        session.add(student)
        session.commit()

        assert student.id is not None

        saved_student = (
            session.query(Student)
            .filter_by(name="Test Student")
            .first()
        )

        assert saved_student is not None
        assert saved_student.name == "Test Student"

    finally:
        session.close()


def test_select_student():
    """
    Перевірка вибірки студента з бази.
    """
    session = Session()

    try:
        student = (
            session.query(Student)
            .filter_by(name="Test Student")
            .first()
        )

        assert student is not None
        assert student.name == "Test Student"

    finally:
        session.close()


def test_update_student():
    """
    Перевірка оновлення студента.
    """
    session = Session()

    try:
        student = (
            session.query(Student)
            .filter_by(name="Test Student")
            .first()
        )

        assert student is not None

        student.name = "Updated Student"
        session.commit()

        updated_student = (
            session.query(Student)
            .filter_by(name="Updated Student")
            .first()
        )

        assert updated_student is not None
        assert updated_student.name == "Updated Student"

    finally:
        session.close()


def test_delete_student():
    """
    Перевірка видалення студента.
    """
    session = Session()

    try:
        student = (
            session.query(Student)
            .filter_by(name="Updated Student")
            .first()
        )

        assert student is not None

        session.delete(student)
        session.commit()

        deleted_student = (
            session.query(Student)
            .filter_by(name="Updated Student")
            .first()
        )

        assert deleted_student is None

    finally:
        session.close()