from find_where import find_where

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 25},
]

result = find_where(data, "name", age=25)
print(result)
