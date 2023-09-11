# Print factors

num = int(input("Input a number: "))


for i in range(1, num+1):
    if num%i == 0:
        print(i)