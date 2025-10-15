from datetime import datetime, timedelta

def days_until_birthday(birthday_month: int, birthday_day: int):
    today = datetime.today()
    current_year = today.year
    next_birthday = datetime(year=current_year, month=birthday_month, day=birthday_day)
    if next_birthday < today:
        next_birthday = datetime(year=current_year + 1, month=birthday_month, day=birthday_day)
    days_left = (next_birthday - today).days
    return days_left

month = 12
day = 25

days_left = days_until_birthday(month, day)
print(f"There are {days_left} day(s) left until your next birthday.")
