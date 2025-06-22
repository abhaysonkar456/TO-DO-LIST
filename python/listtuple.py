# # # # # # # for i in range(1, 101):
# # # # # # #     if '3' in str(i):
# # # # # # #         print("contains3")
# # # # # # #     if i % 3 == 0 and i % 5 == 0:
# # # # # # #             print("fizzbuzz")
# # # # # # #     elif i % 3 == 0:
# # # # # # #             print("Fizz")
# # # # # # #     elif i % 5 == 0:
# # # # # # #             print("Buzz")
# # # # # # #     else:
# # # # # # #             print(i)


# # # # # # for i in range(1, 10, 2):
# # # # # #     print("*" * i)

# # # # # n = 5  # number of rows

# # # # # for i in range(1, n + 1):
# # # # #     # Print spaces
# # # # #     for space in range(n - i):
# # # # #         print(" ", end="")
    
# # # # #     # Print stars
# # # # #     for star in range(2 * i - 1):
# # # # #         print("*", end="")
    
# # # # #     # Move to the next line
# # # # #     print()


# # # # import random

# # # # def guess_the_number():
# # # #     number_to_guess = random.randint(1, 101)
# # # #     attempts = 0

# # # #     print("guess the number between 1 - 100! ")

# # # #     while True:
# # # #         guess = int(input("enter a number: "))
# # # #         attempts += 1

# # # #         if guess < number_to_guess:
# # # #             print("Too low")
# # # #         elif guess > number_to_guess:
# # # #             print("too high")
# # # #         else:
# # # #             print("congratulations you guess the number!", attempts)
# # # #             break

# # # # guess_the_number()

# # # square = [x**2 for x in range(1, 11)]
# # # print(square)

# # even = [x for x in range(1,21) if x % 2 == 0]
# # print(even)

# words = ["apple", "banana", "avocado", "grape", "apricot"]

# a_words = [word for word in words if word.startswith('a')]
# print(a_words)

chars = {char for char in "hello world"}
print(chars)