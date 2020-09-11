<<<<<<< HEAD:4 - Number Checker/Number Checker.py
def checker(num):
    if num % 2 == 0:
        print("Number is even\n")
    else:
        print("Number is odd\n")


print("Even/Odd Number Checker\n")

while True:
    try:
        num = input('Input Number: ')
        checker(int(num))
    except ValueError:
        print('Invalid Input\n')

    continue
=======
def checker(num):
    if num % 2 == 0:
        print("Number is even\n")
    else:
        print("Number is odd\n")


print("Even/Odd Number Checker\n")

while True:
    try:
        num = input('Input Number: ')
        checker(int(num))
    except ValueError:
        print('Invalid Input\n')

    continue
>>>>>>> a509bd990291189bbdd0a33be3065fd529867c9b:Number Checker/Number Checker.py
