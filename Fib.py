
def fib(count):
    myArray = [0,1]
    if (count <= 1):
        return [0]
    for i in range(count - 2):
        myArray.append(myArray[-1] + myArray[-2])
    return myArray

print fib(5)
