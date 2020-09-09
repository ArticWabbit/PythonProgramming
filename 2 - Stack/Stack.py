stack = []

while True:

    def isEmpty(stack):
        return len(stack) == 0


    def push(stack, item):
        stack.append(item)
        return print(item + " pushed to stack\n")


    def pop(stack):
        if (isEmpty(stack)):
            return str(print("Stack is empty\n"))

        else:
            return stack.pop()


    print("Press 1 to push to stack")
    print("Press 2 to pop stack\n")

    userInput = input("What would you like to do?: ")

    if userInput == "1":
        item = input("What would you like to push?: ")
        push(stack, item)

    elif userInput == "2":
        print(pop(stack) + " popped from stack")

        continue
