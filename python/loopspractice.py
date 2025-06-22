# # # # # # # # # #qno 1
# # # # # # # # # i = 1
# # # # # # # # # # for i in range(5):
# # # # # # # # # #     print(i)
# # # # # # # # # #     i += 1

# # # # # # # # # #qno 2
# # # # # # # # # i = 10
# # # # # # # # # for i in range(10):
# # # # # # # # #     if i <= 5:
# # # # # # # # #         print(i)
# # # # # # # # #         i += 1

# # # # # # # # #qno 3
# # # # # # # # for i in range(2, 21, 2):
# # # # # # # #     print(i)

# # # # # # # #qno 4
# # # # # # # total = 0

# # # # # # # for num in range(1, 11):
# # # # # # #     total += 1
# # # # # # #     print("sum:", total) 

# # # # # # num = 21
# # # # # # is_prime = True

# # # # # # if num > 1:
# # # # # #     for i in range(2, num):
# # # # # #         if num % i == 0:
# # # # # #             is_prime = False
# # # # # #             break

# # # # # # if is_prime:
# # # # # #     print("Prime")
# # # # # # else:
# # # # # #     print(" Not Prime")

# # # # # word = "Abhay"
# # # # # for char in word:
# # # # #     print(char)

# # # # fruits = { "apple", "banana", "coconut"}

# # # # for index, fruit in enumerate(fruits):
# # # #     print(index, fruit)

    
# # # #basic level
# # # # for i in range(1, 11):
# # # #     print(i)

# # # i = 1

# # # while i <= 10:
# # #     print(i)
# # #     i += 1


# # # word = "ABHAY"

# # # for i in word:
# # #     print(i)

# # for i in range(2, 21, 2):
# #     print(i)

# i = 10

# while i >= 1:
#     print(i)
#     i -= 1

password = ""
while password != "python123":
    password = input("enter password: ")
print("access granted")

