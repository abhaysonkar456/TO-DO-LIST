# # # # # # # #print sum of number

# # # # # # # n = 5
# # # # # # # sum = 0
# # # # # # # i = 1

# # # # # # # while i <= n:
# # # # # # #     sum += i
# # # # # # #     i += 1

# # # # # # # print("total of sum = ", sum )


# # # # # # # for i in range(1, 6):
# # # # # # #     print(i)

# # # # # # i = 1

# # # # # # while i <= 5:
# # # # # #     print(i)
# # # # # #     i += 1


# # # # # n = int(input("enter a number : "))

# # # # # for i in range(1, 11):
# # # # #     print(n * i)

# # # # sum = 0

# # # # for i in range(2, 101, 2):
# # # #     print(i)

# # # sum_even = 0
# # # for i in range(2, 101, 2):
# # #     sum_even += i

# # #     print("sum of even numbers from 1 to 100 is:", sum_even)

# # i = 10

# # while i >= 1:
# #     print(i)
# #     i -= 1

# numbers = [10, 15, 22, 33, 40, 55]

# for i in numbers:
#     if i % 2 != 0:
#         print(i)

for i in range(1, 5):
    for j in range(i):
        print("*", end =" ")
    print()