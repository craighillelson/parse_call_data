import csv
import datetime
import itertools
import statistics
from get_occurrences_of_weekdays_between_two_dates import days_occurrences
from collections import namedtuple
from datetime import datetime


def convert_string_to_date(a):
    return datetime.strptime(a, "%Y-%m-%d").date()


def import_csv_create_dictionary():
    weekdays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
        )
    lst1 = []
    dct1 = {}
    dct2 = {}

    with open("dates_durations.csv") as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        assembled_tuple = namedtuple('assembled_tuple', headings)
        for detail in f_csv:
            row = assembled_tuple(*detail)
            date = convert_string_to_date(row.date)
            time_object = datetime.strptime(row.time, "%I:%M:%S %p").time()
            lst1.append(time_object)
            day = weekdays[date.weekday()]
            duration = row.duration
            lst2 = duration.split(":")
            hours = int(lst2[0])
            minutes = int(lst2[1])
            seconds = int(lst2[2])
            duration_total = (hours * 3600) + (minutes * 60) + seconds
            duration_decimal = round(duration_total / 60, 2)
            dct1.setdefault(date, []).append(duration_decimal)
            dct2.setdefault(day, []).append(duration_decimal)

    return dct1, dct2


def output_dictionary_with_totals(dct1):
    print(f"\ndate, number of calls")
    dct2 = {}
    for k, v in dct1.items():
        total_calls = len(v)
        dct2[k] = total_calls

    for k, v in sorted(dct2.items(), key=lambda x: x[1], reverse=True):
        print(f"{k}, {v}")


def build_dictionary_with_sums(dct1):
    dct2 = {}
    for k, v in dct1.items():
        total_duration = round(sum(v), 1)
        dct2[k] = total_duration

    return dct2


# def output_dictionary_with_averages(dct1):
#     dct2 = {}
#     for k, v in dct1.items():
#         average = round(statistics.mean(v), 1)
#         dct2[k] = average

    # print("\ndate, average duration")
    # for k, v in sorted(dct2.items(), key=lambda x: x[1], reverse=True):
    #     print(k, v)


def build_dictionary_with_averages(dct1):
    dct2 = {}
    for k, v in dct1.items():
        average = round(statistics.mean(v), 1)
        dct2[k] = average

    return dct2


def output_dictionary_sorted_by_values(header, dct):
    print(header)
    for k, v in sorted(dct.items(), key=lambda x: x[1], reverse=True):
        print(f"{k}, {v}")


def merge_dictionaries(dct1, dct2):
    dct3 = {**dct1, **dct2}

    for key, value in dct3.items():
        if key in dct1 and key in dct2:
            dct3[key] = [value, dct1[key]]

    return dct3


def build_dictionary():
    dct = {}

    for k, v in days_and_durations.items():
        number_of_calls = len(v)
        dct[k] = number_of_calls

    return dct


def output_days_and_total_calls():
    print("\nday, total calls")
    for day, total_calls in sorted(days_and_number_of_calls.items(),
                                   key=lambda x: x[1], reverse=True):
        print(f"{day}, {total_calls}")


def output_average_number_of_calls_per_day():
    print("\nday, average calls per day")
    for day, calls_occurrences in sorted(days_total_calls_occurrences.items(),
                                         key=lambda x: x[1], reverse=True):
        total_calls = calls_occurrences[0]
        number_of_occurrences = calls_occurrences[1]
        average_calls_per_day = round(total_calls / number_of_occurrences, 0)
        print(day, int(average_calls_per_day))


dates_and_durations, days_and_durations = import_csv_create_dictionary()
output_dictionary_with_totals(dates_and_durations)
dates_total_durations = build_dictionary_with_sums(dates_and_durations)
output_dictionary_sorted_by_values("\ndate, total duration",
                                   dates_total_durations)
dates_and_averages = build_dictionary_with_averages(dates_and_durations)
output_dictionary_sorted_by_values("\ndate, average duration",
                                   dates_and_averages)

days_and_number_of_calls = build_dictionary()
output_days_and_total_calls()
days_total_durations = build_dictionary_with_sums(days_and_durations)
output_dictionary_sorted_by_values("\nday, total duration",
                                   days_total_durations)
days_total_calls_occurrences = merge_dictionaries(days_occurrences,
                                                  days_and_number_of_calls)
output_average_number_of_calls_per_day()
days_and_averages = build_dictionary_with_averages(days_and_durations)
output_dictionary_sorted_by_values("\nday, average duration",
                                   days_and_averages)
