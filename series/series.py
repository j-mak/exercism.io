def slices(string, slice_size):
    """Return list of lists with size of given slice size."""
    result = []
    if slice_size <= 0 or slice_size > len(string):
        raise ValueError

    for i in range(len(string) + 1 - slice_size):
        string_slice = string[i:i + slice_size]
        slice_array = []
        for character in string_slice:
            slice_array.append(int(character))
        result.append(slice_array)
    return result
