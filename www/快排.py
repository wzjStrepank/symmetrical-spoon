import time
import random
# from functools import wraps

list1 = list(range(200000,0,-1))
random.shuffle(list1)
# print(list1)


def timer(func):
    # @wraps(func)
    def wrapper(*args):
        a = time.time()
        print(a)
        func(*args)
        b = time.time()
        c = b - a
        print(b)
        print(c)
    return wrapper


@timer
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


quick_sort(list1,0,len(list1)-1)
# print(list1)