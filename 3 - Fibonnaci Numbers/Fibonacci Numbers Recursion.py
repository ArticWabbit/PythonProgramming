while True:

    # Fibonacci Function
    def fib(n):
        # Input Checker
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        # Recursion
        else:
            return fib(n - 1) + fib(n - 2)

    # User Input
    n = int(input("n = "))
    # Function Caller
    print(fib(n))

    continue
