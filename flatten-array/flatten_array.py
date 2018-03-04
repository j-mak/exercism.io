def flatten(deep_array):
    """Returns flatten array."""
    response = []
    for item in deep_array:
        if isinstance(item, list):
            response.extend(flatten(item))
        elif isinstance(item, (str, int)):
            response.append(item)
    return response
