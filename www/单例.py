class Demo(object):
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        if not hasattr(Demo,"_instance"):
            cls._instance = object.__new__(cls)
            # Demo._instance = object.__new__(cls)
            # cls._instance = super().__new__(cls)
            # cls._instance = super(Demo, cls).__new__(cls)
            print(id(Demo._instance))
        return cls._instance


demo01 = Demo("demo01")
demo02 = Demo("demo02")

print(demo01)
print(demo02)

print(id(demo01))
print(id(demo02))
