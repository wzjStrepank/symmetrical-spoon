import time
import random
# from functools import wraps

list1 = list(range(1000,0,-1))
random.shuffle(list1)
# print(list1)


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
def choose_sort01():
    # 从后往前遍历列表下标
    for i in range(len(list1)-1,0,-1):
        # 从第一个元素开始遍历j，比较每一个j下标的元素与i下标元素的大小
        for j in range(0,i+1):
            # 判断i下标元素与j下标元素的大小，如果i下标元素小于等于j下标元素大小，则把两个元素换位，大的元素来到i的下标位置
            # 遍历一轮过后，列表中最大的值来到此时i下标位置，之后的遍历j的最大值为i-1，不会影响到排好序的元素
            if list1[i] <= list1[j]:
                list1[i],list1[j] = list1[j],list1[i]
    print(list1)


@timer
def choose_sort02():
    # 从后往前遍历列表下标
    for i in range(len(list1)-1,0,-1):
        # 假设一个最大元素下标，假设为i
        max_index = i
        # 从前往后遍历i之前的元素，判断j下标元素与max_index下标元素大小
        for j in range(0,i+1):
            # 判断j下标元素与max_index下标元素大小，如果j下标元素大于max_index下标元素大小，则更新假设最大元素下标max_index
            if list1[max_index] < list1[j]:
                max_index = j
        # 遍历一轮过后，列表中最大的值来到此时i下标位置，之后的遍历j的最大值为i-1，不会影响到排好序的元素
        list1[i], list1[max_index] = list1[max_index], list1[i]
    print(list1)

choose_sort01()
choose_sort02()