from datetime import datetime
from calendar import monthrange

import plotly.express as px


def plot_data(data_list, start_date):
    """
    Plots data using Plotly
    """
    data = make_timeline(data_list, start_date)
    fig = px.line(
        data,
        "Date",
        "Amount Available",
        hover_name=lambda d: data[]"Date",
        hover_data=["Change", "Description"],
    )
    fig.update_layout(yaxis_tickprefix="$")
    fig.show()


def make_timeline(data_list, start_date):
    """
    Converts a list of transaction dictionaries into lists of days and amounts.
    """
    dates = []
    amounts = []
    descriptions = []
    changes = []

    for transaction in data_list:
        dates.append(calculate_date(start_date, transaction["day"]))
        descriptions.append(transaction["description"])
        changes.append(transaction["amount"])

    sorted_lists = sorted(zip(dates, descriptions, changes))
    dates, descriptions, changes = zip(*sorted_lists)

    for change in zip(dates, changes):
        last_amount = amounts[-1] if len(amounts) > 0 else 0
        amounts.append(round_float(last_amount + change[1]))

    return {
        "Date": dates,
        "Amount Available": tuple(amounts),
        "Description": descriptions,
        "Change": changes,
    }


def round_float(num, precision=2):
    """
    Rounds the input number to the specified precision. Default is 2.
    """
    return round(num * 10 ** precision) / (10 ** precision)


def calculate_date(date, day):
    """
    Calculates the next calendar date after `date` on which `day` will land. If
    the calculated date falls outside the range of days for the month, the
    highest day for that month will be returned.
    """
    increment_month = False
    increment_year = False
    if day == 0:
        return date
    if day < date.day:
        increment_month = True
    if increment_month & (date.month == 12):
        increment_year = True

    year = date.year + increment_year

    month = date.month + increment_month
    if month > 12:
        month %= 12

    _, max_day_of_month = monthrange(year, month)
    day = day if day <= max_day_of_month else max_day_of_month

    return datetime(year, month, day)
