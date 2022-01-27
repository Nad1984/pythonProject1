def title(func):
    def wrapper(*args, **kwargs):
        return f"CEO Red Bull Inc.\nMr. John Bigbull \n\n{func(*args, **kwargs)}"

    return wrapper


@title
def select_vacation_type(vacation_request_type):
    if vacation_request_type == 1 or vacation_request_type == 3:
        return f"Hi John,\nI need the paid vacations from {from_date} to {to_date}. \n{firstName} {lastName}"
    elif vacation_request_type == 2:
        return f"Hi John,\nI need the the paid sick leave from {from_date} to {to_date}. \n{firstName} {lastName}"


vacation_request_type = int(input('Enter 1 if you need a "Vacation", \nenter 2 if you need a "Sick leave", \nenter 3 if you need a "Day off": '))

firstName = input('Please, enter your first name: ')
lastName = input('Please, enter your surname: ')
from_date = input('Please, enter the start date of the vacation in the form dd-mm-year: ')
to_date = input('Please, enter the end date of the vacation in the form dd-mm-year: ')


print(select_vacation_type(vacation_request_type))