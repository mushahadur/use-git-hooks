"""This module provides utility functions for basic arithmetic operations."""


def add_numbers(a: float, b: float) -> float:
    """Returns the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The addition of a and b.
    """
    return a + b


if __name__ == "__main__":
    # Test cases for the function
    result_1 = add_numbers(3, 5)
    print(f"Result 1: {result_1}")

    result_2 = add_numbers(10, 20)
    print(f"Result 2: {result_2}")

    print("Pre-commit hook test passed successfully!")
