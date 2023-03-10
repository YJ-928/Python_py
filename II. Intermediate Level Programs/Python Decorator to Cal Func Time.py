# To calculate time taken by a function

# Import time
from time import time

# Defining python decorator function


def TimeCalulator(func):

    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print("Execution Time: \t", t2-t1)
        return result
    return wrapper

# Calling the decorator function and assinging randomFuction to it


@TimeCalulator
def randomFucntion(n):
    for i in range(0, n):
        for j in range(0, n):
            temp = i * j
            j -= 1
    return temp


# Calling randomFucntion
randomFucntion(11000)
