# natural numbers

# n = 0

# while n < 10:
#     n = n + 1
#     print(n)


# pattern
# n = 0
# lst = []
# for i in range (1,6):
#     n = n + 1
#     lst.append(n)
#     print(lst)

# pattern

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# sum of number from 1 to a given number
def sum_numbers():
    num = int(input("Enter the number:"))
    sum_of_num = 0

    for i in range(1, num + 1):
        sum_of_num += i

    print("Sum of numbers from 1 to", num, "is:", sum_of_num)

sum_numbers()
