"""
Tests for plot_data
"""
from datetime import datetime
from plot_data import make_timeline, round_float, plot_data_plotly, calculate_date

test_data = [
    {"description": "Current", "day": 0, "amount": 2000.00},
    {"description": "Cell Phone", "day": 8, "amount": -80},
    {"description": "Water Bill", "day": 3, "amount": -50},
    {"description": "Savings", "day": 18, "amount": -100.00},
    {"description": "Mortgage", "day": 1, "amount": -1555.56},
    {"description": "Paycheck", "day": 15, "amount": 500.00},
]


def test_make_timeline():
    """
    Test make_timeline function
    """
    start_date = datetime(2021, 1, 1)
    expect_x = [0, 1, 3, 8, 15, 18]
    expect_y = [2000, 444.44, 394.44, 314.44, 814.44, 714.44]
    expect_desc = [
        "Current",
        "Mortgage",
        "Water Bill",
        "Cell Phone",
        "Paycheck",
        "Savings",
    ]
    expect_date = [
        start_date,
        datetime(2021, 1, 1),
        datetime(2021, 1, 3),
        datetime(2021, 1, 8),
        datetime(2021, 1, 15),
        datetime(2021, 1, 18),
    ]
    assert (expect_x, expect_y, expect_desc, expect_date) == make_timeline(
        test_data, start_date
    )


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


# plot_data_plotly(test_data)
