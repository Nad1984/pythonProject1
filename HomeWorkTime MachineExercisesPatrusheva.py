# Time Machine exercises: Create chronometry function
import time


def count_down_sec():
    count_sec = int(input('How many seconds to count down? '))
    if count_sec > 0:
        while count_sec != 0:
            yield f"Seconds left: {count_sec}"
            time.sleep(1)
            count_sec -= 1
    else:
        print(f"Incorrect number: {count_sec}. Please, enter a positive number: ")


for sec in count_down_sec():
    print(sec)

print("START!!!")


# Time traveling task/ найти дату в столетии

from datetime import date
import random


def get_random_date_with_same_day_and_month(desired_date):
    first_year = desired_date.year // 100 * 100
    last_year = first_year + 100
    year_given_by_time_machine = random.randint(first_year, last_year)
    time_machine_date = date(year_given_by_time_machine, teachers_birthday.month, teachers_birthday.day)
    return time_machine_date


def try_until_find_wish_date(desired_date):
    while True:
        generated_date = get_random_date_with_same_day_and_month(desired_date)
        if generated_date == desired_date:
            print(f"YOU MADE IT!!! The date is {generated_date}")
            break


teachers_birthday = date(1979, 2, 3)
try_until_find_wish_date(teachers_birthday)

for x in range(30):
    desired_date = date(1984, 10, 29)
    first_year = desired_date.year // 10 * 10
    last_year = first_year + 10
    if x >=first_year and x <= last_year:
        print(x)



# find a year in decade
from datetime import date
import random


def get_random_date_with_same_day_and_month(etalon_date):
    first_year = etalon_date.year // 100 * 100
    last_year = first_year + 100
    year_given_by_time_machine = random.randint(first_year, last_year)
    time_machine_date = date(year_given_by_time_machine, teachers_birthday.month, teachers_birthday.day)
    return time_machine_date


def try_until_find_wish_date(etalon_date):
    while True:
        generated_date = get_random_date_with_same_day_and_month(etalon_date)
        if generated_date == etalon_date:
            yield f"YOU MADE IT!!! The date is {generated_date}"
            break


def first_year_in_decade(etalon_date):
    first_year = etalon_date.year // 10 * 10
    return first_year


def last_year_in_decade(first_year):
    last_year = first_year + 10
    return last_year


teachers_birthday = date(1979, 2, 3)
etalon_date = teachers_birthday
first_year = first_year_in_decade(etalon_date)
last_year = last_year_in_decade(first_year)

print(next(try_until_find_wish_date(teachers_birthday)))


for x in range(30):
    current_date = get_random_date_with_same_day_and_month(etalon_date)
    if first_year <= current_date.year <= last_year:
        print(current_date)