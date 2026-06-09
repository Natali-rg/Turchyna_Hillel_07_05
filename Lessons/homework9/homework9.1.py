class Rhombus:
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більше 0")

        if name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут повинен бути в межах від 0 до 180 градусів")

            object.__setattr__(self, "angle_b", 180 - value)

        object.__setattr__(self, name, value)

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def show_info(self):
        print(f"Сторона a: {self.side_a}")
        print(f"Кут A: {self.angle_a} градусів")
        print(f"Кут B: {self.angle_b} градусів")


# Створення ромба
side_a = int(input("Введіть сторону А "))
angle_a = int(input("Введіть кут А "))
rhombus = Rhombus(side_a, angle_a)

# Виведення інформації
rhombus.show_info()

# Зміна кута A
angle_a_change = int(input("Введіть зміни для кута А "))
rhombus.angle_a = angle_a_change

print("\nПісля зміни кута A:")
rhombus.show_info()