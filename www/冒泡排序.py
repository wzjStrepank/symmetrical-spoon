import time
import random
# from functools import wraps

list00 = list(range(20000,0,-1))
random.shuffle(list00)
# print(list00)


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
def demo():
    # 从后往前遍历列表下标
    for i in range(len(list00)-1,0,-1):
        # 从第一个元素遍历到第i个元素，每次遍历时判断当前元素与下一个元素的大小
        for j in range(i):
            # 判断当前元素与下一个元素的大小，如果当前元素大于下一个元素，则两个元素换位，大的向后走
            # 一轮过后，最大的元素会到达最后的位置，之后的遍历的j的最大值为下一个i-1
            if list00[j] > list00[j+1]:
                list00[j],list00[j+1]=list00[j+1],list00[j]
    print(list00)

demo()