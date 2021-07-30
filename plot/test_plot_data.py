"""
Tests for plot_data
"""
from plot_data import make_timeline, round_float, plot_data

test_data = [
    {"description": "Current", "day": 0, "amount": 2000.00},
    {"description": "Water Bill", "day": 3, "amount": -50},
    {"description": "Cell Phone", "day": 8, "amount": -80},
    {"description": "Mortgage", "day": 1, "amount": -1555.56},
    {"description": "Paycheck", "day": 15, "amount": 500.00},
    {"description": "Savings", "day": 18, "amount": -100.00},
]


def test_make_timeline():
    """
    Test make_timeline function
    """
    expect_x = [0, 1, 3, 8, 15, 18]
    expect_y = [2000, 444.44, 394.44, 314.44, 814.44, 714.44]
    assert [expect_x, expect_y] == make_timeline(test_data)


def test_round_float():
    """
    Test round_float function
    """
    assert round_float(3.1415926535) == 3.14
    assert round_float(5.36598789756, 3) == 5.366


plot_data(test_data)
