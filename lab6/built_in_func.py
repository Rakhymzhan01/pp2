from functools import ((reduce))
import time
import math

def multiply_list(numbers):
    if not numbers:
        return None

    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [1, 2, 3, 4, 5]

result = multiply_list(numbers)
print("Result:", result)


def count_upper_lower(string):
    # Initialize counters for uppercase and lowercase letters
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = "Hello World"

upper, lower = count_upper_lower(input_string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

input_string = "awsswa"

if is_palindrome(input_string):
    print("Is a palindrome.")
else:
    print("Not a palindrome.")


def calculate_square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")

# Sample input
number = 25100
milliseconds = 2123

calculate_square_root_after_delay(number, milliseconds)

def all_elements_true(tuple_input):
    return all(tuple_input)

my_tuple = (True, True, False, True)

result = all_elements_true(my_tuple)
print("All elements of the tuple are true:", result)
