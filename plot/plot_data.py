import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


def plot_data(data_list):
    """
    Plots a list of transaction dictionaries
    """
    x_vals, y_vals = make_timeline(data_list)
    plt.plot(x_vals, y_vals)
    plt.xlabel("Date")
    plt.ylabel("Amount Available")
    plt.show()


def make_timeline(data_list):
    """
    Converts a list of transaction dictionaries into lists of days and amounts.
    """
    x_vals = []
    y_vals = []
    for transaction in sorted(data_list, key=lambda t: t["day"]):
        last_amount = y_vals[-1] if len(y_vals) > 0 else 0
        x_vals.append(transaction["day"])
        y_vals.append(round_float(last_amount + transaction["amount"]))
    return [x_vals, y_vals]


def round_float(num, precision=2):
    """
    Rounds the input number to the specified precision. Default is 2.
    """
    return round(num * 10 ** precision) / (10 ** precision)
