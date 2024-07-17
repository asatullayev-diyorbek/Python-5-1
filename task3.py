from datetime import datetime


def check_date(date1, date2):
    difference_days = abs(date1 - date2)
    return difference_days


if __name__ == "__main__":
    sana1 = datetime(2024, 4, 23).date()
    sana2 = datetime(2024, 7, 24).date()

    print(f"{sana1} va {sana2} orasidagi kunlar soni: {check_date(sana1, sana2).days}")
