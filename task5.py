import calendar


def calendar_year_html(year):
    html_cal = calendar.HTMLCalendar(calendar.SUNDAY)
    yil_html = ""
    for month in range(1, 13):
        yil_html += html_cal.formatmonth(year, month)
    return yil_html


if __name__ == '__main__':
    yil = 2024
    print(f"{yil} yil uchun kalendar HTML formatda:")
    print(calendar_year_html(yil))
