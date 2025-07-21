def multiply_numbers(a, b)
    # SyntaxError: missing colon after function definition
    return a * b

def get_list_element(lst, index):
    # IndexError: index out of range if index >= len(lst)
    return lst[index]

def greet_user(name):
    # TypeError: trying to concatenate str and int
    greeting = "Hello, " + name + 123
    print(greeting)

if __name__ == "__main__":
    print(multiply_numbers(2, 3))
    print(get_list_element([1, 2, 3], 5))
    greet_user("Alice")
