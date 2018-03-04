import re


def decode(encoded_string):
    """Return plain string."""

    response = []
    groups = re.findall(r"(\d+[a-zA-Z\ ]|[a-zA-Z\ ])", encoded_string)

    for item in groups:
        if len(item) > 1:
            count = item[:-1]
            char = item[-1]
            response.append(char * int(count))
        else:
            response.append(item)
    return "".join(response)


def encode(plain_string):
    """Return encoded string."""

    response = []
    groups = re.findall(r"(([a-zA-Z\ ])\2*)", plain_string)

    for item in groups:
        count = len(item[0])
        char = item[1]
        if count > 1:
            response.append(str(count) + char)
        else:
            response.append(char)
    return "".join(response)
