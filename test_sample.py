# def add_two_numbers(a, b):
#     return a + b

# def test_adds_two_numbers():
#     # Arrange
#     a = 7
#     b = 12
#     expected = 19

#     # Act
#     result = add_two_numbers(a, b)

#     # Assert
#     assert result == expected

# print(test_adds_two_numbers())


# def add_two_numbers(a, b):
#     return a + b

# # No class needed (but can use)
# def test_answer():
#     assert add_two_numbers(3, 5) == 9

# content of test_sample.py

import pytest

def add_two_numbers(a, b):
    return a + b

# No class needed (but can use)
def test_answer():
    assert add_two_numbers(3, 5) == 5


# print(add_two_numbers(1, 1)) # Expected 2
# print(add_two_numbers(-1, 0)) # Expected -1
# print(add_two_numbers(1.00234, 0.3456)) # Expected 1.34794
# print(add_two_numbers("string 1", "string 2")) # Expected Error
# print(add_two_numbers("test", 1)) # Expected Error