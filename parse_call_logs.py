import csv
import datetime
import itertools
import statistics
from collections import namedtuple
from datetime import datetime


def convert_string_to_date(a):
    return datetime.strptime(a, "%Y-%m-%d").date()


def import_csv_create_dictionary():
    dct = {}

    with open("dates_durations.csv") as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        assembled_tuple = namedtuple('assembled_tuple', headings)
        for detail in f_csv:
            row = assembled_tuple(*detail)
            date = convert_string_to_date(row.date)
            time_object = datetime.strptime(row.time, "%I:%M:%S %p").time()
            duration = row.duration
            lst = duration.split(":")
            hours = int(lst[0])
            minutes = int(lst[1])
            seconds = int(lst[2])
            duration_total = (hours * 3600) + (minutes * 60) + seconds
            duration_decimal = round(duration_total / 60, 2)
            time_duration = (time_object, duration_decimal)
            dct.setdefault(date, []).append(time_duration)

    return dct


def output_results():
    days = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        )
    date_times_durations = import_csv_create_dictionary()
    for date, call_details in date_times_durations.items():
        print(f"\ndate: {date}")
        day = days[date.weekday()]
        print(f"day: {day}")
        times = []
        durations = []
        for i in call_details:
            times.append(i[0])
            duration = i[1]
            durations.append(duration)
        print(f"total duration: {round(sum(durations), 2)}")
        print(f"average duration: {round(statistics.mean(durations), 2)}")
        print(f"total calls: {len(call_details)}")
        if len(times) > 1:
            for num, call_time in enumerate(times, 1):
                print(f"{num}. {call_time}")
        else:
            print(*times)


output_results()
