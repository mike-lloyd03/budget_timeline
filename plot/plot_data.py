from datetime import datetime
from calendar import monthrange
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


def plot_data(data_list):
    """
    Plots a list of transaction dictionaries
    """
    x_vals, y_vals, _ = make_timeline(data_list)
    plt.plot(x_vals, y_vals)
    plt.xlabel("Date")
    plt.ylabel("Amount Available")
    plt.show()


def plot_data_plotly(data_list):
    """
    Plots data using Plotly
    """
    x_vals, y_vals, descriptions = make_timeline(data_list)
    data = {"Day": x_vals, "Amount Available": y_vals, "Description": descriptions}
    fig = px.line(data, "Day", "Amount Available", hover_name="Description")
    fig.update_layout(yaxis_tickprefix="$")
    fig.show()


def make_timeline(data_list, start_date):
    """
    Converts a list of transaction dictionaries into lists of days and amounts.
    """
    days = []
    amounts = []
    descriptions = []
    dates = []
    for transaction in sorted(data_list, key=lambda t: t["day"]):
        last_amount = amounts[-1] if len(amounts) > 0 else 0
        days.append(transaction["day"])
        amounts.append(round_float(last_amount + transaction["amount"]))
        descriptions.append(transaction["description"])
        dates.append(calculate_date(start_date, transaction["day"]))
    return (days, amounts, descriptions, dates)


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
