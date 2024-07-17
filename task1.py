import datetime


def week_day_number(date):
    number = date.weekday()
    return number + 1


if __name__ == "__main__":
    sana = datetime.date.today()
    print(f"{sana} sanasining hafta kuni tartib raqami: {week_day_number(sana)}")
