people = [
    ('John', 'Smith', 28, 'Developer', 'London'),
    ('Emma', 'Brown', 34, 'Designer', 'Paris'),
    ('Michael', 'Johnson', 45, 'Manager', 'Berlin'),
    ('Olivia', 'Williams', 31, 'Teacher', 'Madrid'),
    ('Daniel', 'Jones', 26, 'Engineer', 'Rome'),
    ('Sophia', 'Miller', 38, 'Doctor', 'Warsaw'),
    ('James', 'Davis', 29, 'Lawyer', 'Prague'),
    ('Isabella', 'Garcia', 41, 'Architect', 'Vienna'),
    ('Ethan', 'Martinez', 33, 'Chef', 'Lisbon'),
    ('Mia', 'Rodriguez', 27, 'Nurse', 'Dublin'),
    ('Alexander', 'Wilson', 36, 'Pilot', 'Oslo'),
    ('Charlotte', 'Anderson', 24, 'Photographer', 'Helsinki'),
    ('Benjamin', 'Thomas', 32, 'Programmer', 'Stockholm'),
    ('Amelia', 'Taylor', 39, 'Scientist', 'Copenhagen')
]

# 1. Add your new record o the beginning of the given list

my_record = ('Oleksii', 'Ivanov', 30, 'QA Automation Engineer', 'Warsaw')
people.insert(0, my_record)

# 2. In modified list swap elements with indexes 1 and 5 (1<->5). Print result

people[1], people[5] = people[5], people[1]

print("Modified list:\n")
for person in people:
    print(person)

# 3. check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

result = (
    people[6][2] >= 30 and
    people[10][2] >= 30 and
    people[13][2] >= 30
)

print("\nAge check result:")
print(result)