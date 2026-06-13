class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)

        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


# Тест
teamlead = TeamLead("Ivan",5000,"QA","Python",5)

print(teamlead.__dict__)

assert "department" in teamlead.__dict__
assert "programming_language" in teamlead.__dict__

print("Тест пройдено успішно!")