def transform(entry_data):
    """Converting entry data from key-value to value-key."""
    response = {}
    for key, value in entry_data.items():
        for item in value:
            response.update({item.lower(): key})

    return response
