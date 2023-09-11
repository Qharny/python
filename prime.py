# generate a prime numbers

number = int(input("Enter a number: "))


for num in range(0, number):
    if num >1:
        for i in range (2,num):
            if (num % i) == 0 :
                break
        else:
            print(num)