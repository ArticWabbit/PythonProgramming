def checker(num):
    if num % 2 == 0:
        print("Number is even\n")
    else:
        print("Number is odd\n")


print("Even/Odd Number Checker\n")

while True:
    num = int(input('Input Number: '))
    checker(num)

    continue
