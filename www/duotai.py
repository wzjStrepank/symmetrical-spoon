class People(object):
    name = "xiaoming"  # 公有的属性
    __age = 12  # 私有属性

    # 创建People类的对象


p = People()
print(p.name)  # ok
print(People.name)  # ok
# print(p.__age)    # no ok   不能在类外面通过实例对象访问类的私有属性
# print(People.__age)  # no ok   不能通过类对象访问私有属性


