import pytest
from find_where import find_where

# Sample data for testing
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]


def test_find_where_returns_correct_value():
    result = find_where(data, "name", age=25)
    assert result == "Bob"


def test_find_where_raises_value_error_for_invalid_data_type():
    with pytest.raises(ValueError):
        find_where("invalid_data", "name", age=25)


def test_find_where_raises_value_error_for_no_matching_dictionary():
    with pytest.raises(ValueError):
        find_where(data, "name", age=40)


def test_find_where_raises_value_error_for_key_not_found():
    with pytest.raises(ValueError):
        find_where(data, "invalid_key", age=25)
