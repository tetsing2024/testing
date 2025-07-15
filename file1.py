#!/usr/bin/env python3
"""
A simple Python file with an intentional indentation bug.
This demonstrates a common syntax error that can occur in Python.
"""

def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two integers."""
    result = a + b
return result


def main() -> None:
    try:
        x = 10
        y = 20
        total = calculate_sum(x, y)
        print(f"The sum of {x} and {y} is: {total}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main() 
