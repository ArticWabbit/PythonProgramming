def makeStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")

def pop(stack):
    if (isEmpty(stack)):
        return str(print("No items in stack"))

    return stack.pop()

stack = makeStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped")
print(pop(stack) + " popped")
print(pop(stack) + " popped")
print(stack)

input("\n#####")