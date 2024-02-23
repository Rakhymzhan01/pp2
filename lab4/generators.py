#Create a generator that generates the squares of numbers up to some number N.
def squares_up_to_N(N):
    for i in range(1, N + 1):
        yield i ** 2

# Example usage:
N = int(input())
squares_generator = squares_up_to_N(N)

for square in squares_generator:
    print(square)

#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

N = int(input("Enter a number (N): "))

even_numbers_generator = even_numbers(N)

even_numbers_list = list(even_numbers_generator)

print("Even numbers up to", N, ":", ", ".join(map(str, even_numbers_list)))

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
def main():
    n = int(input("Enter the upper limit (n): "))
    generator = divisible_by_3_and_4(n)
    print("Numbers divisible by 3 and 4 between 0 and", n, "are:")
    for num in generator:
        print(num, end=" ")

if __name__ == "__main__":
    main()

#Implement a generator that returns all numbers from (n) down to 0.
def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1


# Test the generator with a for loop
def main():
    n = int(input("Enter a number (n): "))

    print(f"Numbers from {n} down to 0:")
    for num in numbers_down_to_zero(n):
        print(num)


if __name__ == "__main__":
    main()
