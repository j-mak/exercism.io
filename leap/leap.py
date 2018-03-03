def is_leap_year(year):
    """This method verify if given year is leap or not."""
    return not year % 4 and ((year % 100) or (not year % 400))
