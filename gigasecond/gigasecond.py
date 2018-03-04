import datetime


def add_gigasecond(given_time):
    """Add giga second to given time."""
    delta = datetime.timedelta(seconds=10**9)
    given_time += delta
    return given_time
