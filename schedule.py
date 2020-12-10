"""Returns a function of the time period for class"""

import time


class TimeInfo:
    """Contains Time Info"""

    def __int__(self, current_period='None', next_period='None'):
        self.current_period = current_period
        self.next_period = next_period


def check_time():
    """Returns the current period of class."""
    current_time = time.localtime()

    minutes_of_day = (int(current_time.tm_hour) * 60) + int(current_time.tm_min)

    periodinfo = TimeInfo()

    if minutes_of_day < 435:
        periodinfo.current_period = "The School Day hasn't started yet."
        periodinfo.next_period = "Next Period will be at 7:15."
    elif 435 <= minutes_of_day <= 471:
        periodinfo.current_period = "It is currently Period 1."
        periodinfo.next_period = "The period will end at 7:51."
    elif 475 < minutes_of_day < 475:
        periodinfo.current_period = "Currently in-between classes."
        periodinfo.next_period = "The next period will start at 7:55."
    elif 475 <= minutes_of_day <= 505:
        periodinfo.current_period = "It is currently Period 2."
        periodinfo.next_period = "The period will end at 8:25."
    elif 505 < minutes_of_day < 509:
        periodinfo.current_period = "Currently in-between classes."
        periodinfo.next_period = "The next period will start at 8:29."
    elif 509 <= minutes_of_day <= 539:
        periodinfo.current_period = "Currently in Period 3."
        periodinfo.next_period = "The period will end at 8:59."
    elif 539 < minutes_of_day < 543:
        periodinfo.current_period = "Currently in-between classes."
        periodinfo.next_period = "The next period will start at 9:03."
    elif 543 <= minutes_of_day <= 573:
        periodinfo.current_period = "Currently in Period 4."
        periodinfo.next_period = "The period will end at 9:33."
    elif 573 < minutes_of_day < 577:
        periodinfo.current_period = "Currently in-between classes."
        periodinfo.next_period = "The next period will start at 9:37."
    elif 577 <= minutes_of_day <= 607:
        periodinfo.current_period = "Currently in Period 5."
        periodinfo.next_period = "The period will end at 10:07."
    elif 607 < minutes_of_day < 611:
        periodinfo.current_period = "Currently in-between classes."
        periodinfo.next_period = "The next period will start at 10:11."
    elif 611 <= minutes_of_day <= 641:
        periodinfo.current_period = "Currently in Period 6."
        periodinfo.next_period = "The period will end at 10:41."
    elif 641 < minutes_of_day < 645:
        periodinfo.current_period = "Currently in-between classes."
        periodinfo.next_period = "The next period will start at 10:45."
    elif 645 <= minutes_of_day <= 675:
        periodinfo.current_period = "Currently in Period 7."
        periodinfo.next_period = "The school day will end at 11:15."
    else:
        periodinfo.current_period = "School is not in session"
        periodinfo.next_period = "After School meets are from 12:22 to 1:51. Don't forget to join."

    return periodinfo
