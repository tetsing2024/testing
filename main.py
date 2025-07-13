#!/usr/bin/env python3
"""
Simple Calculator Application with a Bug

This is a demo application for SWE-agent that contains a bug in the division function.
The bug is that division by zero doesn't handle the error properly.
"""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
    # BUG: This function doesn't handle division by zero properly
    # It should raise a ValueError with a descriptive message
    if b == 0:
        raise ValueError('Division by zero is not allowed')
    return a / b

def main():
    """Main function to demonstrate the calculator."""
    print("Simple Calculator Demo")
    print("=====================")
    
    # Test basic operations
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    
    # This will cause an error due to the bug
    try:
        result = divide(10, 0)
        print(f"10 / 0 = {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 
