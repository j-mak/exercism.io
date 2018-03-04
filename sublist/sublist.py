SUBLIST = -1
EQUAL = 0
SUPERLIST = 1
UNEQUAL = 255


def check_lists(list_a, list_b):
    if list_a == list_b:
        return EQUAL
    elif is_sublist(list_a, list_b):
        return SUBLIST
    elif is_sublist(list_b, list_a):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sublist(first, second):
    start = 0
    end = len(first)
    while end <= len(second):
        if first == second[start:end]:
            return True
        start, end = start + 1, end + 1
    return False
