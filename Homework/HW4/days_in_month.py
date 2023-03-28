# Write a function named days_in_month that accepts a month (an integer between 1 and 12) as a parameter and returns the number of days in that month. For example, the call days_in_month(9) would return 30 because September has 30 days. Assume tat the code is not being run during a leap year (that Februrary always has 28 days). The following are the number of days in each month:
#
# January 31
# February 28
# March 31
# April 30
# May 31
# June 30
# July 31
# August 31
# September 30
# October 31
# November 30
# December 31
#
# Write your function here
def days_in_month(month):
    if month == 1:
        return 31
    elif month == 2:
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31
    else:
        return "Invalid month"