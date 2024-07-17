from task5 import calendar_year_html
from task3 import check_date
import os
from datetime import datetime


def save_calendar(year, file_name) -> None:
    if not os.path.exists(file_name):
        data = calendar_year_html(year)
        with open(file_name, 'w') as file:
            file.write(data)
            print("Saqlandi!")
    else:
        print("File avvaldan mavjud!")


def day_of_birthday(day: int, month: int, year: int):
    birthday = datetime(year, month, day).date()
    today = datetime.today().date()
    birthday_this_year = birthday.replace(year=today.year)

    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year+1)

    days = check_date(birthday_this_year, today).days
    years_old = check_date(today.year, birthday.year)

    if days == 0:
        return f"Bugun tug'ilgan kuningiz. {years_old} yoshingiz muborak🥳!"
    return f"Tug'ilgan kuningizgacha: {days} kun qoldi.\n {years_old} yoshga to'lasiz"


if __name__ == "__main__":
    save_calendar(2024, 'calendar.html')
    print(day_of_birthday(13, 7, 2004))
