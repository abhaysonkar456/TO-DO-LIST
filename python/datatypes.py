# # # # # # # n = int(input("enter a number: "))
# # # # # # # largest_num = None
# # # # # # # for i in range(n):
# # # # # # #      num = int(input(f"enter number { i + 1}: "))
# # # # # # #      if largest_num is None or num > largest_num:
# # # # # # #           largest_num = num

# # # # # # # print(largest_num)

# # # # # # n = int(input("enter a number: "))
# # # # # # i = 1

# # # # # # while i <= 10:
# # # # # #     print(n * i)
# # # # # #     i += 1

# # # # # # print("loop ended")

# # # # # list = ( 1, 12, 33, 54, 85, 106)
# # # # # i = 0
# # # # # x = 33
# # # # # while i <= len(list)-1:
# # # # #     if list[i] == x:
# # # # #         print("found at idx", i)
# # # # #     else:
# # # # #         print("finding... ")
# # # # #     i += 1


# # # # n = [1, 5, 11, 18, 25, 31, 38]
# # # # x = 31
# # # # i = 0
# # # # while i <= len(n)-1:
# # # #     print(n[i])
# # # #     i += 1
# # # #     if n == x:
# # # #         print("found")
# # # #         if n >= x:
# # # #             print("too high")
# # # #         else:
            
# # # #             print("too low")

# # # import random
# # # secret_number = random.randint(1, 100)
# # # guess = None

# # # while guess != secret_number:
# # #     guess = int(input("guess the number (1 - 100): "))
# # #     if guess < secret_number:
# # #         print("Too low")
# # #     elif guess > secret_number:
# # #         print("Too high")
# # #     else:
# # #         print("Correct ! you guess it")

# # answer = ""
# # while answer.lower() != "yes":
# #     answer = input("please type 'yes' to continue: ")
# #     if answer == "yes":
# #         print("Thanks")
# #     else:
# #         print("Wrong text")

# list = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in list:
#     print(val)  

n = int(input("enter a number: "))
for i in range(1, 11):
    print(n * i)
    