from collections import Counter
from datetime import (timedelta,
                      date)


def daterange(date1, date2):
    for i in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(i)


def create_a_list_of_dates():
    lst = []
    start_date = date(2021, 3, 1)
    end_date = date(2021, 5, 31)
    for calendar_date in daterange(start_date, end_date):
        lst.append(calendar_date)

    return lst, start_date, end_date


def create_a_list_of_days():
    weekdays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        )
    lst = []
    for day in dates:
        weekday = weekdays[day.weekday()]
        lst.append(weekday)

    return lst


def output_count_of_days():
    day_counts = Counter(days)
    return dict(day_counts.most_common())


dates, start, end = create_a_list_of_dates()
days = create_a_list_of_days()
days_occurrences = output_count_of_days()
