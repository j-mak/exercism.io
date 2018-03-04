import datetime
import calendar

week = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, week_day, descriptor):
    """Calculate mext meetup day."""
    first_weekday, month_days = calendar.monthrange(year, month)

    i = 1

    valid_days = []

    for i in range(1, month_days + 1):
        if week[datetime.date(year, month, i).weekday()] == week_day:
            valid_days.append(datetime.date(year, month, i))

    if descriptor == 'teenth':
        for t in valid_days:
            if 13 <= t.day <= 19:
                return t
    elif descriptor == 'last':
        return valid_days[-1]
    else:
        try:
            num = int(descriptor[0])
            return valid_days[num - 1]
        except IndexError:
            raise MeetupDayException
