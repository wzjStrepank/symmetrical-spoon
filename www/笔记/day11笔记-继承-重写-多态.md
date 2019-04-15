私有
自定义异常
## 11.01_Python语言基础(继承的介绍)(掌握)
* 继承的概念：
	* 在现实生活中，一般指子女继承父辈的财产
* 程序中的继承：
	* 继承描述的是事物之间的所属关系，之前的猫，狗----》动物
	* 程序中可以描述猫和狗继承动物
               object
#          
               		动物
        	 猫               狗
  		加菲    波斯       金毛   二哈





## 11.02_Python语言基础(单继承)(掌握)
* 生活中的单继承：
	* 孩子只能有一个亲生父亲或者母亲
* 程序中的单继承：
	* 子类只能有一个父类--》子类只能继承一个父类
####单继承案例：
#
	# 定义一个父类
	class Cat(object):
	    def __init__(self, name, color):
	        self.__name = name
	        self.color = color
	
	    def run(self):
	        print("%s----在跑" % self.__name)
	
	
	# 定义一个子类
	class Bosi(Cat):
	    def setNewName(self, newName):
	        self.__name = newName
	
	    def eat(self):
	        # print("%s---在吃饭"%self.__name)
	        pass
	
	
	bs = Bosi("波斯", "白色")
	# print(bs.__name)
	print(bs.color)
	bs.eat()
	
	bs.setNewName("加菲")
	bs.eat()
	bs.run()


>**说明：**<br/>
虽然在子类中没有定义__init__()方法
但是父类有，在子类继承父类的时候这个方法也就被继承过来
创建Bosi对象，默认执行那个继承过来的__init__方法
***   
   
>**总结：**<br/>
子类在继承的时候，在定义类的时候，小括号中为父类的名字
父类的公有属性和公有方法会被子类继承
***
### 再赠送一个案例
#
	print("父类中出现私有的情况")
	
	# 定义一个父类
	class Animal(object):
	    def __init__(self, name="动物", color="白色"):
	        self.__name = name
	        self.color = color
	
	    def __test(self):
	        print(self.__name)
	        print(self.color)
	
	    def test(self):
	        print(self.__name)
	        print(self.color)
	
	
	# 定义一个子类
	class Dog(Animal):
	
	    def Test1(self):
	        # print(self.__name)#不能访问父类的私有属性
	        print(self.color)
	
	    def dogTest2(self):
	        # self.__test()#不能访问父类的私有方法
	        self.test()
	
	
	a = Animal()
	
	# print(a.__name)#报错，不能通过对象访问私有属性
	# a.__test()#报错，不能访问私有方法
	a.test()
	print("--------")
	
	d = Dog(name="小花狗", color="黄色")
	print(d.color)
	d.Test1()
	d.dogTest2()


>**总结：**<br/>
私有的属性，不能通过对象直接访问，可以通过方法进行访问<br/>
私有方法，不能通过对象直接访问<br/>
私有属性，方法都不会被子类继承，也不能被访问<br/>
子类继承的是父类公有是属性和方法
***







## 11.03_Python语言基础(多继承)(掌握)

* 生活中的例子：
	* 骡子是马和驴的杂交品种
* 程序中的多继承：
	* 一个子类有多个父类，并且据有他们的特征，这被称为多继承
# 
	# 定义一个父类
	class A:
	    def printA(self):
	        print("----A-----")
	
	
	# 定义一个父类
	class B:
	    def printB(self):
	        print("----B-----")
	
	
	# 多继承
	class C(A, B):
	    def printC(self):
	        print("----C-----")
	
	
	# 创建C的对象
	c = C()
	c.printA()
	c.printB()
	c.printC()


>**说明：**<br/>
python中可以多继承<br/>
父类中的方法和属性，子类会继承
***


#### 多个父类中出现相同的方法案例：
#
	print("多个父类中出现相同的方法")
	
	
	# 如果父类A和B,有一个同名的方法，
	# 那么子类在调用方法的时候，执行哪个父类中的方法
	# 定义一个父类
	class A:
	    def printA(self):
	        print("----A-----")
	
	
	# 定义一个父类
	class B:
	    def printA(self):
	        print("----B-----")
	
	
	# 多继承
	class C(A, B):
	    pass
	
	
	c = C()
	c.printA()
	
	print(c)
	
	
	# 案例：
	
	class base(object):
	    def test(self):
	        print("base--test")
	
	
	class D(base):
	    def test(self):
	        print("D----test")
	
	
	class E(base):
	    def test(self):
	        print("E----test")
	
	
	class F(D, E):
	    pass
	
	
	f = F()
	f.test()
	print(F.__mro__)  # 可以查看类的对象搜索方法时的先后顺序


>**练习：**<br/>
有一个学校，人数为0，如果有新入职的老师和学生，那么人数增加1，要显示他的信息：
老师要显示姓名和工号，学生要显示姓名和成绩<br/>
    使用继承<br>
    父类   学校<br>
    子类   老师   学生
***

#### 参考代码：
#
	print("练习题")
	
	
	# 学校类
	class School:
	    # 定义默认的人数为0
	    schoolNum = 0
	
	    # 初始化数据
	    def __init__(self, name):
	        self.name = name
	        School.schoolNum += 1
	        print("学校新加入的成员：%s" % self.name)
	        print("学校现有的学生的人数%s" % School.schoolNum)
	
	    # 自我介绍，姓名和工号，成绩
	    def sayHello(self):
	        print("我叫%s" % self.name)
	
	
	# 创建老师类
	class Teacher(School):
	    def __init__(self, name, id):
	        a = School(name)
	        self.name = name
	        self.id = id
	
	    def sayHello(self):
	        print("我叫%s,工号为%d" % (self.name, self.id))
	
	
	# 学生类
	class Student(School):
	    def __init__(self, name, result):
	        self.name = name
	        self.result = result
	        b = School(name)
	
	    def sayHello(self):
	        print("我叫%s,成绩：%d" % (self.name, self.result))
	
	
	# 创建老师对象
	t = Teacher("小明", 1000)
	t.sayHello()
	s = Student("张三", 99)
	s.sayHello()






## 11.04_Python语言基础(重写父类的方法和调用父类的方法)(掌握)

* 重写：
    * 就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖父类中的方法
#### 重写父类方法
	#定义一个父类
	class Cat(object):
	    def sayHello(self):
	        print("hello----1")
	#定义子类
	class Bosi(Cat):
	    def sayHello(self):
	        print("hello -------2")
	#创建子类的对象
	bs = Bosi()
	bs.sayHello()


想一想：要求打印出hello ------1,该如何实现	


#### 调用父类属性
#
	class Cat(object):
	    def __init__(self, name):
	        self.name = name
	        self.color = "yello"
	
	class Bosi(Cat):
	    def __init__(self, name):
	        self.name = name
	        # 方式1调用父类__init__方法,python2中/python3中
	        # Cat.__init__(self,name)
	        # 方式2：super(),可以完成对父类__init__()的调用
	        # super(Bosi,self).__init__(name)
	        # 方式3：super()直接调用__init__()函数
	        super().__init__(name)

	
	# super()#一层一层向上
	bosi = Bosi("xiaoming")
	print(bosi.name)
	print(bosi.color)








## 11.05_Python语言基础(多态)(掌握)

* 多态：
   * 定义的类型和运行时的类型不一样----》多态
* Python并不支持真正的多态
* Python中使用伪代码来实现多态

#### Python多态案例：
#
	class F1(object):
	    def show(self):
	        print("F1.show")
	
	class S1(F1):
	    def show(self):
	        print("S1.show")

	class S2(F1):
	    def show(self):
	        # super().show()
	        print("s2.show")
	        # F1.show(self)
	        # super(S2,self).show()

	# python  动态的言语

	def func(F1):
	    print("func接受一个数据类型")
	    # print(F1.show())
	# func(F1)
	
	# s1 = S1()
	# s1.show()
	s2 = S2()
	s2.show()








## 11.06_Python语言基础(类属性和实例属性)(掌握)

> **概述：**<br/>
类属性就是类对象所拥有的属性，它被所有类对象的实例对象所公有<br/>类属性在内存中只存一个副本对于公有类属性和实例属性在类的外面可以直接被访问


#### 类属性

* 类属性：
    * 在类中定义的属性（公有和私有）
    * 定义位置：类中方法外
###类属性案例：
#
	# 定义一个类:
	class People(object):
	    name = "xiaoming"  # 公有的属性
	    __age = 12  # 私有属性
	
	
	# 创建People类的对象
	p = People()
	print(p.name)  		# ok
	print(People.name)  # ok
	# print(p.__age)    # no ok   不能在类外面通过实例对象访问类的私有属性
	print(People.__age)	# no ok   不能通过类对象访问私有属性


### 实例属性
#
	# 定义类
	class People(object):
	    address = "北京"
	
	    def __init__(self):
	        self.name = "xiaoming"  # 实例属性
	        self.age = 12  			# 实例属性
	
	
	p = People()
	p.age = 20
	print(p.age)
	print(p.name)
	print(p.address)
	
	print(People.address)
	# print(People.name)  #类对象访问实例属性
	# print(People.age)   #类对象访问实例属性


#### 通过实例对象去修改类属性

#
	print("@" * 20)
	
	class People(object):
	    country = "china"
	
	    def __init__(self):
	        self.name = "hhaa"
	
	print(People.country)
	p = People()
	print(p.country)
	p.country = "chinese"  # 实例属性会屏蔽同名的类属性
	print(p.country)
	print(People.country)
	
	del p.country
	print(p.country)


#### 总结

#
	如果需要在类外修改类属性，必须通过类对象去引用再进行修改
	如果通过实例对象去引用，会产生一个同名的实例属性，
	这个方式其实是修改实例属性，不会影响类属性，
	并且之后如果需要通过实例对象去引用该同名的属性，
	实例属性会强制屏蔽类属性，即引用的是类属性，除非删除该实例属性
	
	类属性
	    类所有拥有的属性
	    调用
	        类属性可以被类直接调用
	        实例对象可以调用类属性
	    修改
	        类对象不能修改实例属性
	        类对象可以修改类属性
	
	实例属性
	    属于实例对象的属性
	    调用
	        不能直接被类调用
	        实例对象能调用实例属性
	    修改
	        实例对象可以修改实例属性
	        实例对象不能修改类属性
	    如果实例属性和类属性重名
	        实例对象在调用时优先使用实例属性
	        类对象在调用时优先使用类属性






## 11.07_Python语言基础(静态方法和类方法)(掌握)
#### 类方法


> **类方法:**<br/>
   类对象所拥有的方法，需要使用到修饰器 @classmethod---->类方法<br/>
   对于类方法，第一个参数必须是类对象，一般以cls表示作为第一个参数<br/>
  （当然可以用其他的名字，但是不建议修改）

#
	class People(object):
	    country = "china"
	
	    @classmethod
	    def getCountry(cls):
	        return cls.country
	
	
	p = People()
	print(p.country)
	print(p.getCountry())		#通过实例对象进行访问
	print(People.country)
	print(People.getCountry())  # 通过类对象去引用


	print("#" * 20)
	
	
	p = People()
	print(p.country)
	print(p.getCountry())  		# 通过实例对象进行访问
	print(People.country)
	print(People.getCountry())  # 通过类对象去引用
	
	
	class People(object):
	    country = "china"
	
	    # 类方法
	    @classmethod
	    def getCountry(cls):
	        return cls.country
	
	    @classmethod
	    def setCountry(cls, country):
	        cls.country = country
	
	
	p = People()
	print(p.getCountry())  		# 可以用实例对象引用
	print(People.getCountry())	# 通过类对象的的引用
	
	p.setCountry("chinese")
	print(p.getCountry())
	print(People.getCountry())

#### 作用:
* 类方法可以对类属性进行修改

* 发现规律:
  * 结果显示在用类方法对类属性进行操作修改之后,通过类对象和实例对象访问都发生了变化


#### 静态方法

* 定义：
	* 需要通过修饰器@staticmethod来进行修饰，不需要传参数

#
	print("#" * 20)
	
	
	class People(object):
	    country = "china"
	
	    # def getCountry(self):
	    #     return " "
	    @staticmethod
	    def getCountry():
	        return People.country
	
	
	print(People.getCountry())
	p = People()
	print(p.getCountry())



#### 总结
#
	从类方法和实例方法（普通方法）和静态方法
	类方法第一个参数是类对象cls,那么通过cls的引用必定是类对象的属性和方法
	实例方法第一个参数self,自身，那么通过self引用的可能是类属性，也可以是实例属性（具体分析）

	问题？
	如果出现相同名称的类属性和实例属性
	实例属性优先级更高
	静态方法：静态方法中不需要传递任何参数（额外的定义参数），
	在静态方法中的引用是类属性，必须通过类对象来引用



with

自定义异常
## 11.15_Python语言基础(抛出自定义异常)(掌握)

* 如何定义一个自定义的异常
	* 需要使用raise语句用来引发异常
	* 异常和错误对象必须有一个名字，并且是error或者是exception的子类

* raise 语句的基本的格式
* raise 自定义的异常类的对象
#
	#自定义的异常类
	class ShortInputException(Exception):
	    def __init__(self, length):
	        self.length = length
	        self.atLeast = 6
	
	    def __str__(self):
	        return "ShortInputException: 最小长度要求是6,,您输入的是%d" % self.length
	
	
	try:
	    password = input("请输入密码:")
	    if len(password) < 6:
	        # raise 抛出异常
	        raise ShortInputException(len(password))
	except ShortInputException as e:
	    print(e)
	else:
	    print("密码长度合法")
单例模式