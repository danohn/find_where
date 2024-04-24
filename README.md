# find_where

`find_where` is a Python package that provides a function to find values in dictionaries where a specified key matches a given value, similar to filtering in SQL.

## Installation

You can install `find_where` using pip:

    pip install find_where

## Usage

    from find_where import find_where

    # Sample data

    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]

    # Find the value for the key "name" where the age is 25

    result = find_where(data, "name", age=25)
    print(result)  # Output: "Bob"
