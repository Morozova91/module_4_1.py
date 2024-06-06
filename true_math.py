import math


def divide(first, second):
    if second == 0:
        return math.inf
    else:
        return first / second


res1 = divide(3, 4)
print(res1)
res2 = divide(3, 0)
print(res2)
