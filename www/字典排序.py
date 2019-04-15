demo_dict = {"a": 1, "b": 3, "d": 6, "e": 3, "f": 2, "c": 5}
print(demo_dict.keys())
print(demo_dict.values())
print(demo_dict.items())

# 根据key排序
a = sorted(demo_dict)
print(a)
# items提取键值对后，默认根据键排序
b = sorted(demo_dict.items())
print(b)
c = sorted(demo_dict.items(),key=lambda x: x[0])
print(c)

# 根据value排序
d = sorted(demo_dict.values())
print(d)
e = sorted(demo_dict.items(),key=lambda x: x[1])
print(e)

