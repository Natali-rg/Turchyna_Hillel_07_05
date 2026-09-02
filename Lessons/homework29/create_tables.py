from database import engine, Base
from models import Student, Course

Base.metadata.create_all(engine)

print("Tables created successfully!")