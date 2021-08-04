"""
Tests for plot_data
"""
from datetime import datetime
from plot_data import make_timeline, round_float, plot_data, calculate_date

START_DATE = datetime(2015, 3, 7)
TEST_DATA = [
    {"description": "Current", "day": 0, "amount": 2000.00},  # 20150307
    {"description": "Water Bill", "day": 3, "amount": -50},  # 20150403
    {"description": "Savings", "day": 18, "amount": -100.00},  # 20150318
    {"description": "Mortgage", "day": 1, "amount": -1555.56},  # 20150401
    {"description": "Cell Phone", "day": 8, "amount": -80},  # 20150308
    {"description": "Paycheck", "day": 15, "amount": 500.00},  # 20150315
]


def test_make_timeline():
    """
    Test make_timeline function
    """
    expect_dates = (
        datetime(2015, 3, 7),
        datetime(2015, 3, 8),
        datetime(2015, 3, 15),
        datetime(2015, 3, 18),
        datetime(2015, 4, 1),
        datetime(2015, 4, 3),
    )
    expect_amounts = (2000, 1920, 2420, 2320, 764.44, 714.44)
    expect_desc = (
        "Current",
        "Cell Phone",
        "Paycheck",
        "Savings",
        "Mortgage",
        "Water Bill",
    )
    expect_change = (2000, -80, 500, -100, -1555.56, -50)
    expect = {
        "Date": expect_dates,
        "Amount Available": expect_amounts,
        "Description": expect_desc,
        "Change": expect_change,
    }
    assert expect == make_timeline(TEST_DATA, START_DATE)


def test_round_float():
    """
    Test round_float function
    """
    assert round_float(3.1415926535) == 3.14
    assert round_float(5.36598789756, 3) == 5.366


def test_calculate_date():
    """
    Test calculate_date
    """
    # Same day
    assert calculate_date(datetime(2021, 1, 1), 0) == datetime(2021, 1, 1)
    # Within same month
    assert calculate_date(datetime(2021, 1, 1), 15) == datetime(2021, 1, 15)
    # Next month
    assert calculate_date(datetime(2021, 1, 28), 15) == datetime(2021, 2, 15)
    # Next month and year
    assert calculate_date(datetime(2021, 12, 28), 15) == datetime(2022, 1, 15)
    # Day out of range
    assert calculate_date(datetime(2021, 1, 30), 29) == datetime(2021, 2, 28)
    # Day not out of range for leap year
    assert calculate_date(datetime(2020, 1, 30), 29) == datetime(2020, 2, 29)
    # On same day
    assert calculate_date(datetime(2021, 1, 1), 1) == datetime(2021, 1, 1)


# plot_data_plotly(test_data, datetime(2021, 8, 3))
