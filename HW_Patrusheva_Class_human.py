# Завдання №1
#
# Розробити клас Людина. Людина має:
#
# Ім'я
# Прізвище
# Вік (атрибут але ж змінний)
# Стать
# Люди можуть:
#
# Їсти
# Спати
# Говорити
# Ходити
# Стояти
# Лежати
# Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо
# в __init__. Треба сказати, що доступ до статичних полів класу з __init__ не можу іти через
# НазваКласу.статичий_атрибут, позаяк ми не може бачити імені класу. Але натомість ми можемо
# сказати self.__class__.static_attribute.

class Human:
    __count_human = 0

    def __init__(self, name, surname, age, gender):
        Human.__count_human += 1
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

        def to_eat(self, food):
            return f"I like eating this {food}."

        def to_sleep(self, hours):
            return f"I like to sleep for {hours} hours."

        def talk(self):
            return f"I like to talk to my friends."

        def walk(self, distance):
            return f"I like to walk for a {distance}km."

        def stand(self, time):
            return f"I hate to be in a que for {time} minutes."

        def rest(self, time):
            return f"I'd like to rest fo {time}hours."

    @staticmethod
    def get_count_human():
        return Human.__count_human

    def is_it_max_population_now(self):
        current_human_count = Human.get_count_human()
        if max_population == current_human_count:
            return f"The population increased to max level now, its {max_population} people."
        else:
            return f"It is not yet max population."


max_population = 3

katya_vasukova = Human("Katya", "Vasukova", "29", "female")
print(katya_vasukova.surname)
print(Human.get_count_human())
print(katya_vasukova.is_it_max_population_now())

maxim_dobrodelov = Human("Maxim", "Dobrodelov", "25", "male")
print(maxim_dobrodelov.get_count_human())
print(maxim_dobrodelov.is_it_max_population_now())

zina_naduvaeva = Human("Zina", "Naduvaeva", "45", "female")
print(zina_naduvaeva.get_count_human())
print(zina_naduvaeva.is_it_max_population_now())



