import time
import random
# from functools import wraps

list1 = list(range(200000,0,-1))
random.shuffle(list1)


def timer(func):
    # @wraps(func)
    def wrapper():
        a = time.time()
        print(a)
        func()
        b = time.time()
        c = b - a
        print(b)
        print(c)
    return wrapper


@timer
def demo01():
    def suan(list, p, r):
        if p < r:
            s = pai(list, p, r)
            suan(list, p, s)
            suan(list, s + 1, r)
    i = 0
    def pai(list, p, r):
        i = p - 1
        for j in range(p, r):
            if list[j] <= list[r]:
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i + 1], list[r] = list[r], list[i + 1]
        return i
    suan(list1, 0, len(list1) - 1)


demo01()
# print(list1)

