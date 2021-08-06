import csv
import datetime
import itertools
import statistics
from collections import namedtuple


def convert_string_to_date(a):
    return datetime.datetime.strptime(a, "%Y-%m-%d").date()


date_times_durations = {}
with open("dates_durations.csv") as csv_file:
    f_csv = csv.reader(csv_file)
    headings = next(f_csv)
    assembled_tuple = namedtuple('assembled_tuple', headings)
    for detail in f_csv:
        row = assembled_tuple(*detail)
        date = convert_string_to_date(row.date)
        time = row.time
        duration = row.duration
        lst = duration.split(":")
        hours = int(lst[0])
        minutes = int(lst[1])
        seconds = int(lst[2])
        duration_total = (hours * 3600) + (minutes * 60) + seconds
        duration_decimal = round(duration_total / 60, 2)
        time_duration = (time, duration_decimal)
        date_times_durations.setdefault(date, []).append(time_duration)

date_number_of_calls = {}
durations = []
assembled_stats = []
for date, details in date_times_durations.items():
    number_of_calls = len(details)
    date_number_of_calls[date] = number_of_calls
    for duration in details:
        durations.append(duration[1])
    average_duration = round(statistics.mean(durations), 2)
    date_calls_duration = (date, number_of_calls, average_duration)
    assembled_stats.append(date_calls_duration)

print("\ndate, number of calls, average duration")
for date_calls_average_duration in assembled_stats:
    print(*date_calls_average_duration, sep=", ")

date_times = {}
for date, details in date_times_durations.items():
    for time in details:
        date_times.setdefault(date, []).append(time[0])

print("\ndate, times")
for date, times in date_times.items():
    print(date, *times, sep=", ")

print("\ndate, number of calls")
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)
for date, number_of_calls in sorted(date_number_of_calls.items(), \
                                    key=lambda x: x[1], reverse=True):
    day = days[date.weekday()]
    print(day, date, number_of_calls)

print("\n")
