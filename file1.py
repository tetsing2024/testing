def calculate_sum(a, b):
    # This function has a syntax error - missing colon after if statement
    if a > 0
        return a + b
    else:
        return b

def divide_numbers(x, y):
    # This function has a NameError - undefined variable
    result = x / y
    return result + undefined_variable

def print_message():
    # This function has an IndentationError
    print("Hello World")
  print("This line has wrong indentation")

# Main execution
if __name__ == "__main__":
    # This will cause multiple errors when run
    print(calculate_sum(5, 3))
    print(divide_numbers(10, 2))
    print_message() 
