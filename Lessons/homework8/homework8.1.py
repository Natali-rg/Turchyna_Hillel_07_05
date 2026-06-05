class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade


    def show_info_student(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")

student1 = Student("Nataliia", "Turchyna", 30, 50)

print("Інформація про студента")
student1.show_info_student()

student1.change_average_grade(65)

print("\nІнформація після зміни середнього балу:")
student1.show_info_student()