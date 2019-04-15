import time
import random
# from functools import wraps

list01 = list(range(10000,0,-1))
# random.shuffle(list01)



def timer(func):
    # @wraps(func)
    def wrapper():
        a = time.time()
        # print(a)
        func()
        b = time.time()
        c = b - a
        # print(b)
        print(c)
    return wrapper


@timer
def demo01():
    def demo(list00):
        if len(list00) >= 2:
            left, right = [], []
            mid = list00[len(list00)//2]
            list00.remove(mid)
            for i in list00:
                if i > mid:
                    right.append(i)
                else:
                    left.append(i)
            return demo(left) + [mid] + demo(right)
        else:
            return list00
    print(demo(list01))


demo01()


