#Function 1
from itertools import permutations
import math
import random

def gram_to_ounch(n):
    return 28.3495231 * n

def fahrenheit(n):
    return (5 / 9) * (n - 32)

def puzzle (head, legs):
    for chicken in range(head):
        rabbit = head - chicken
        total_legs = 2 * chicken + 4 * rabbit
        if total_legs == legs:
            return chicken, rabbit
    return "no solution"

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    index_0 = None
    index_0_7 = None

    for i, num in enumerate(nums):
        if num == 0:
            if index_0 is None:
                index_0 = i
            else:
                index_0_7 = i
                if 7 in nums[index_0 + 1:index_0_7]:
                    return True
    return False

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Example usage:
word = input()
if is_palindrome(word):
    print("Palindrome.")
else:
    print("Not a palindrome.")

def histogram(numbers):
    for num in numbers:
        print('*' * num)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break