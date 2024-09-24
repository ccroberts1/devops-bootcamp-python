from datetime import datetime

def get_birthday():
    user_input = input("Tell me your birthday in the format DD.MM and I'll tell you how far away it is!")
    user_input_list = user_input.split(".")
    birth_day = int(user_input_list[0])
    birth_month = int(user_input_list[1])

    current_datetime = datetime.today()
    birth_current_year = datetime(current_datetime.year, birth_month, birth_day)
    birth_next_year = datetime(current_datetime.year + 1, birth_month, birth_day)

    day_count = 0
    if birth_current_year > current_datetime:
        day_count = birth_current_year - current_datetime
    else:
        day_count = birth_next_year - current_datetime

    print(f"{day_count.days} until your birthday!")