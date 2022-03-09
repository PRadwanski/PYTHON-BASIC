"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime

my_date = '2019-04-13'

def calculate_days(date):
    try:
        pattern = "%Y-%m-%d"
        d1 = datetime.strptime(date, pattern)
        d2 = datetime.today()
        return (d2-d1).days
    except(ValueError, TypeError):
        raise Exception('WrongFormatException')

calculate_days(my_date)

# Tests

def test_calculate_dates():
    date = '2022-03-07'
    assert calculate_days(date) == 1

def test_calculate_dates_future():
    date = '2022-03-10'
    assert calculate_days(date) == -2

def test_calculate_dates_now():
    date = datetime.strftime(datetime.today(),"%Y-%m-%d")
    assert calculate_days(date) == 0
