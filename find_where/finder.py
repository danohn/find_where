def find_where(data, return_key, **kwargs):
    """
    Find values in dictionaries where the key is a given value.

    Args:
    - data (dict or list): The dictionary or list of dictionaries to search.
    - return_key (str): The key whose corresponding value should be returned.
    - **kwargs: Keyword arguments specifying the key-value pairs to match.

    Returns:
    - Any: The value of the specified key in the matching dictionary.

    Raises:
    - ValueError: If `data` is not a dictionary or a list of dictionaries,
                  or if `return_key` is not found in the matching dictionary.
    """
    if not isinstance(data, (dict, list)):
        raise ValueError("data must be a dictionary or a list of dictionaries")

    if isinstance(data, dict):
        data = [data]

    matching_dicts = [d for d in data if all(d.get(k) == v for k, v in kwargs.items())]

    if not matching_dicts:
        raise ValueError("No matching dictionary found")

    if len(matching_dicts) == 1:
        return matching_dicts[0][return_key]

    return [match[return_key] for match in matching_dicts]
