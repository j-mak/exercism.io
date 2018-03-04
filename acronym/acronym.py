import re


def abbreviate(long_name):
    """Returns abbreviate for given name."""
    out = re.findall(r'(?<=[\W])\w', long_name)
    abbr = [x.upper() for x in out]
    return long_name[0] + "".join(abbr)
