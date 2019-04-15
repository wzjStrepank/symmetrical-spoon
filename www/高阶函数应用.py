# reduce,累积
from functools import reduce
print(reduce(lambda x, y: x + y, range(101)))

# filter,过滤器
import calendar
print(list(filter(lambda year: calendar.isleap(year), range(2000,3001))))

# map，映射
print(list(map(lambda x: x**2, range(10))))

# partial,偏函数
from functools import partial


def get_sum(x,y):
    return x + y


demo = partial(get_sum, y=5)
print(demo(10))
ret = partial(lambda x, y: x / y, y=5)
print(ret(10))

