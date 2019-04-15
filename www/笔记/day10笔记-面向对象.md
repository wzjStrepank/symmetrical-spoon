## 10.01_Python语言基础(面向对象思想)(理解)

#### 面向对象的思想
#
	思考：
	   请用程序描述如下事件：
	      A同学报道等级信息
	      B同学报道等级信息
	      C同学报道等级信息
	      A同学做自我介绍
	      B同学自我介绍
	      c同学自我介绍
 
#
	"""
	请用程序描述如下事件：
	      A同学报道等级信息
	      B同学报道等级信息
	      C同学报道等级信息
	      A同学做自我介绍
	      B同学自我介绍
	      c同学自我介绍
	"""
	stu_a = {"name":"A","age":21}
	stu_b = {"name":"B","age":22}
	stu_c = {"name":"C","age":23}
	
	def stu_infor(stu):
	    for key,value in stu.items():
	        print("key = %s,value = %d"%(key,value))
	
	"""


#### 面向过程：
	根据业务逻辑从上到下写代码


   
#### 面向对象：
	将数据与函数绑定到一起，进行封装，能够更快速的开发程序，减少代码的重写的过程
     
	def 发送邮件(内容):
	    # 连接邮箱服务器
	    # 发送邮件
	    # 关闭连接





## 10.02_Python语言基础(类和对象)(掌握)


* 类和对象的概述


#### 对象和类
#
	对象是面向对象思想的核心
	在使用对象的过程中，为了将具有共同特征和行为的一组对象抽象定义-----》类
	类---》制造飞机的图纸
	用它来创建的飞机就相当于对象


#### 类
	具有相似的内部状态和运动规律的实体的集合（抽象）
	或者具有相同的属性和行为的统称
	
	定义：
	  类  抽象的  在使用的时候通常会找到这个类的具体的存在----》对象
	  特点：
	     使用这个具体的存在，一个类可以找到多个对象,一个类可以创建多个对象


#### 对象

	概述：
	   某一个具体事物的存在，在现实世界中可以看得见摸得着
	可以直接使用
	
	总结：
	  类和对象之间的关系：
	     就像利用玩具模型来创建多种不同的玩具
	     类就是创建对象的模板


#### 区分类和对象

	奔驰汽车   	类
	奔驰smart   	类
	张三的那辆奔驰smart    对象
	
	狗    类
	大黄狗   类
	李四家的那只大黄狗    对象
	
	水果    	类
	苹果   	类
	红苹果 	类   红富士苹果   类
	张三嘴里吃了一半的苹果   对象





## 10.03_Python语言基础(类的构成)(掌握)
#### 类的构成
#
	类（class）：由3部分组成
	类的名称：类名
	类的属性：一组数据
	类的方法：允许对其操作的方法（行为）


#### 设计一个人  类
#	
	"""
	事物的名称（类名）：人（Person）
	属性：身高  年龄
	方法（行为）：跑，吃饭
	
	"""
	"""
	狗  类
	类名：dog
	属性：品种，毛色，性别，腿的数量
	方法：叫，跑，咬人，摇尾巴
	"""





## 10.04_Python语言基础(类的抽象)(掌握)
#### 如何把日常生活中的事物抽象成程序中的类？
#
	类：
	    拥有相同属性和行为的对象可以抽取出来-----》类
	    
	一般名称提炼法
	例如：
	 1.坦克发射了3颗炮弹炸掉了2架飞机
	 坦克-----》抽象成类
	 炮弹-----》抽象成类
	 飞机-----》抽象成类
	 
	 2.小明在公车上牵了一条叼着热狗的狗
	 小明  -----》	人类
	 公车  -----》	交通工具类
	 热狗  -----》	食物类
	 狗    -----》	狗类

 
#### 游戏中的类和对象
#
	cf
	人
	枪
	
	植物大战僵尸：
	向日葵   -----》类
	    类名：xrk
	    属性：颜色，尺寸
	    行为：产生阳光
	    
	豌豆：   ------》   类
	    类名：  wd
	    属性：颜色，发型
	    行为：发射炮弹  
	僵尸：
	    类名：js
	    属性：颜色，
	    行为：走，吃植物，啃





## 10.05_Python语言基础(定义类)(掌握)

#### 定义一个类的格式：
#
	class 类名:
		属性1
		属性2
		属性3
		... ...

		方法1
		方法2
		方法3
		... ...


#### 定义类--猫
#
	"""
	猫：
	   类名：cat
	   属性:毛色，性别
	   行为：跑，吃
	"""
	class Cat:
	    #属性
	
	    #方法
	    def eat(self):
	        print("猫吃鱼....")
	
	    def drink(self):
	        print("猫喝可乐....")

	
#### 定义类--车
#
	"""
	车：
	   类名：Car
	   属性:颜色，
	   行为：跑
	"""
	class Car:
	    #方法列表
	    def getCarInfo(self):
	        print("车的轮子数：%d,颜色%s"%())
	
	    def move(self):
	        print("车子在移动....")
	



## 10.06_Python语言基础(经典类和新式类)(熟练)
#### 新式类：
	* Python2.2使用了经典类
	* Python3.X之后默认都是新式类
   	* 在类名后面(object)，Car(object)

* 说明：
    * 定义类的时候有两种，新式类和经典类，上面定义Car为经典类
    * 如class Car(object): 是新式类
    * class Cat: 是经典类
    
>注意：
	定义类名时，尽量使用大驼峰命名法则<br />
	类中的属性命名要见名知意
***







## 10.07_Python语言基础(创建对象)(掌握)

#### python中，可以根据已经定义好的类来创建一个一个的对象

* 创建对象的格式：对象名 = 类名()

#### 创建一个Car类
#
	#创建一个Car类
	class Car(object):
	    def move(self):
	        print("车子在移动....")
	    def toot(self):
	        print("车子在鸣笛....")
	
	
	#创建车子的对象，并用变量进行保存
	BMW = Car()
	BMW.color = "黑色"#车子的颜色
	BMW.wheelNum = 4#车轮的数量
	BMW.color = "白色"
	BMW.move()
	BMW.toot()
	print(BMW.color)
	print(BMW.wheelNum)
	

#### 总结：
	BMW = Car():这样就产生了一个Car的实例对象，
	此时可以通过实例对象BMW访问属性和行为
	BMW--->对象，它拥有属性和行为


#### 为对象添加属性

* 下面以Cat类为例子,添加属性
#
	class Cat:
	    def eat(self):
	        print("猫在吃鱼.....")
	    def drink(self):
	        print("猫在和芬达....")
	        
	#创建一个Cat对象
	tom = Cat()
	#调用tom指向的对象中的方法
	tom.eat()
	tom.drink()
	tom.name = "汤姆"
	tom.age = 3



#### 获取对象的属性
	class Cat:
	    def eat(self):
	        print("猫在吃鱼.....")
	    def drink(self):
	        print("猫在和芬达....")
	
	#创建一个Cat对象
	tom = Cat()
	#调用tom指向的对象中的方法
	tom.eat()
	tom.drink()
	tom.name = "汤姆"
	tom.age = 3
	print("tom的中文名：%s,年龄：%d"%(tom.name,tom.age))





## 10.08_Python语言基础(__init__方法和self的作用)(掌握)
####  init方法是初始化函数，用来完成一些对象默认的设置

* init方法格式

#
	class 类名：
	     #初始化函数，用来完成一些默认的设置
	     def __init__(self):
	            函数体语句


* __init__（）方法调用
	* 下面以汽车类Car示例init方法的调用
#
	# 第一种方式
	
	class Car:
	    # 初始化方法
	    def __init__(self):
	        self.color = "黑色"
	        self.wheelNum = 4
	
	    # 普通的方法，移动
	    def move(self):
	        print("车子在移动.....")
	
	
	# 创建对象
	bmw = Car()
	print("车子的颜色：%s" % bmw.color)
	print("车子的轮子数:%d" % bmw.wheelNum)
	bmw1 = Car()
	print("车子的颜色：%s" % bmw1.color)
	print("车子的轮子数:%d" % bmw1.wheelNum)


>**总结：**
  当创建Car对象后，在没有调用__init__()函数的前提下，
bmw就默认拥有了两个属性color/wheelNum，
原因是__init__()函数在创建对象后，就立刻默认被调用
***


* 还有另一种方式能更灵活的使用init方法
#
	#第二种方式
	
		class Car:
		    #初始化方法
		    def __init__(self,newWheelNum,newColor):
		        self.wheelNum = newWheelNum
		        self.color = newColor
		    #普通的方法，移动
		    def move(self):
		        print("车子在移动.....")
		#创建对象
		bmw = Car(4,"黄色")
		print("车子的颜色：%s"%bmw.color)
		print("车子的轮子数:%d"%bmw.wheelNum)
		bmw1 = Car(6,"绿色")
		print("车子的颜色：%s"%bmw1.color)
		print("车子的轮子数:%d"%bmw1.wheelNum)




>**总结：**
   __init__():在创建一个对象的时候默认被调用，不需要手动调用
   __init__(self),默认一个参数名字为self,不需要开发者传递
   python 解释器会自动将当前的对象的引用传递进来
***





## 10.09_Python语言基础(__del__()方法(析构方法))(熟练)

* 创建对象后，python解释器默认调用__init__()
* 当删除一个对象的时候，python解释器也会默认调用__del__()


###### 分析下面案例
	import sys

	class Cat(object):
	    def __init__(self):
	        self.color = "while"
	        self.weight = "8斤"
	
	    def __del__(self):
	        print("所有对象被干掉啦")
	
	    def __str__(self):
	        return ("颜色%s-体重%s" % (self.color, self.weight))
	
	
	Tom01 = Cat()
	print("Tom01即将被干掉,当前Tom01引用指向地址被引用数量%s" % sys.getrefcount(Tom01))
	Tom02 = Tom01
	Tom03 = Tom02
	print(Tom01)
	print(Tom02)
	print(Tom03)
	
	print("Tom01即将被干掉,当前Tom01引用指向地址被引用数量%s" % sys.getrefcount(Cat))
	print(id(Cat))
	del Tom01
	
	print("Tom02即将被干掉,当前Tom02引用指向地址被引用数量%s" % sys.getrefcount(Tom02))
	print("Tom02即将被干掉,当前Tom03引用指向地址被引用数量%s" % sys.getrefcount(Tom03))
	print("Tom02和Tom03引用指向地址是相同的吗?", Tom02 == Tom03)
	del Tom02
	print("Tom02被干掉啦")
	
	# del Tom03
	# print("Tom03被干掉啦")
	print("我是程序结尾的一句话")
	print("-" * 30)
	
	print(Tom03)
	print(repr(Tom03))
	print(eval(repr(Tom03)))



* **总结**：
   * 当有1个变量保存了对象的引用，此时对象的引用计数加1
   * 当使用__del__()函数的时候，删除的是变量指向的对象时，
   * 如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1
   * 即变为2，当再次调用del 此时会通用删除引用计数，直到变量的引用计数为0
   * 此时才会将变量指向的对象真正删除
   * 获取对象计数:sys.getrefcount(object))
***





## 10.10_Python语言基础(创建多个对象)(掌握)
#### 同一个类可以创建多个对象,比如常见的猫有加菲和Tom
#
	class Cat:
	    def eat(self):
	        print("猫吃鱼....")
	    def drink(self):
	        print("猫喝水....")
	  
	#创建tom 对象       
	tom = Cat()
	tom.eat()
	tom.drink()
	#给tom指向的对象添加两个属性
	tom.name = "汤姆"
	tom.age = 2
	
	
	jiafei = Cat()
	jiafei.eat()
	jiafei.drink()
	jiafei.name = "加菲"
	jiafei.age = 3
#### 同意个类创建的多个对象是相互独立的






## 10.11_Python语言基础(魔方方法)(掌握)

* 魔方方法：
	* 魔法方法是Python中的特殊方法
	* 魔方方法是指指被包含下划线的方法或者所能调用的方法的统称
	* 这些统方法在特殊的情况下被调用，并且基本没有手动调用它的必要
        
#### 下面我们看一下使用Cat类编写的案例
	#定义类
	class Car:
	    def __init__(self,newWheelNum,newColor):
	        self.wheelNum = newWheelNum
	        self.color = newColor
	
	    def __str__(self):
	        msg = "嘿嘿....我的颜色是"+self.color+"我有"+self.wheelNum+"个轮子"
	        return msg
	
	    def move(self):
	
	        print("车子在移动....")
	
	#创建一个对象
	bmw = Car("4","白色")
	print(bmw)

>**总结:**
在python中方法名如果是__XXX__那么就具有特殊的功能，---》魔方
__str__():
当使用print输出对象，只要定义了__str__()方法，
那么就会返回这个方法中return 的数据
***





## 10.12_Python语言基础(__str__和__repr__())(掌握)
* __str__和__repr__()
	* __repr__()与__str__()函数的功能类似
	* __str__()用于将数值转化为人阅读的形式
	* __repr__()转化为python解释器读取的形式


__str__():在调用print打印对象的时候自动调用，给用户用的，是一个描述对象的方法
__repr__():给机器用的，供python的解释器读取

注意：
   在没有__str__（）函数时，有__repr__()，str == repr

#
	import datetime
	
	now = datetime.datetime.now()
	print(str(now))
	print(repr(now))
	print(eval(repr(now)))


>说明：
datetime   python的内置模块，import 加载导入模块
now = datetime.datetime.now()系统当前的时间赋值给now变量
eval函数是把参数当做代码执行，验证repr之后的字符串可以被python识别执行
***
#
	class Person(object):
	    def __init__(self,name,age,height,weight):
	        self.name = name
	        self.age = age
	        self.height = height
	        self.weight = weight
	    def __str__(self):
	        return "%s-%d-%d-%d"%(self.name,self.age,self.height,self.weight)
	
	#创建人的对象
	per = Person("hanmeimei",20,170,55)
	
	print(per)
	print(repr(per))
	# print(eval(repr(per)))#eval函数中的参数为一个字符串，如果不是一个字符串会报错
	aa = "hello"
	print(repr(aa))
	print(eval(repr(aa)))


>
**优点：**
   当一个对象的属性过多，并且还要打印，重写__str__()方法简化代码的书写
   可读性强
***






## 10.13_Python语言基础(构造方法)(掌握)
* 定义：
	* 构造方法类似__init__()函数，差别在于一个对象被构建好之后会自定调用该方法
   	* python中创建一个构造方法（使用__init__())
#
	class Cat:
		def __init__(self):
             初始化属性






## 10.14_Python语言基础(重写__init__()和__str__()方法)(掌握)
* 概述：
    * Python中所有的类都直接或间接继承object
    * object中有__init__()和__str__()方法
    * object中的这两个方法大部分时间和我们使用时的需求不匹配
    * 我们可以根据自己的需求对方法体进行更改,这就叫做重写
    * 更多内容在明天的知识点继承中
* 重写方法使用总结:
	* 当两个关联的类，出现了相同的函数名，在调用该函数时，先在本类中找，
	* 如果有，调用
	* 如果没有，在去父类找，如果有调用，
	* 如果没有，去基类，找不到报错

>重写对于类很重要：
   尤其对于构造  __init__
***
   
#
	class Bird():
	    def __init__(self):
	        self.hungry = True
	
	    def eat(self):
	        if self.hungry:
	            print(".....")
	            self.hungry = False
	        else:
	            print("no thanks")
	b = Bird()
	b.eat()
	b.eat()

>**重写的定义：**
   在子类中定义了一个和父类同名的函数---》重写
***





## 10.15_Python语言基础(理解self)(掌握)
#
	#定义一个类
	class Animal:
	    def __init__(self,name):
	        self.name = name
	    def printName(self):
	        print("名字为：%s"%self.name)
	
	#定义一个函数
	def myPrint(animal):
	    animal.printName()
	
	#创建对象
	dog1 = Animal("西西")
	myPrint(dog1)
	
	dog2 = Animal("北北")
	myPrint(dog2)
	
	
>* 总结：
	* 所谓self理解为自己,也就是对象自身
	* 程序中的self是什么?哪个对象调用了__init__(),self就代表谁
***





## 10.16_Python语言基础(应用-烤牛排)(掌握)
#

	"""
	烤牛排:
	类:
	    类名:
	        牛排:
	    属性:
	        几成熟
	            0--3表示生的,4--6表示半生不熟,7--9表示熟了,10及以上表示糊了
	        红酒
	        胡椒
	        ... ...
	    行为:
	        烧烤时间
	        添加佐料
	        __init__()
	        __str__()
	
		"""
	
	
	class CookSteak:
	    def __init__(self):
	        self.time = 0
	        self.cook_level = 0
	        self.cook_string = "生的"
	        self.condiments = []
	
	    def cook(self, time):
	        self.cook_level += time
	        if self.cook_level > 9:
	            self.cook_string = "扔了吧,都糊啦"
	        elif self.cook_level > 6:
	            self.cook_string = "熟了,味道应该很棒"
	        elif self.cook_level > 3:
	            self.cook_string = "半生不熟,快要熟了"
	        elif self.cook_level > 0:
	            self.cook_string = "牛排刚放进去,耐性等一会"
	        else:
	            print("没有这个状态")
	        print("牛排已经烤了很久了,现在达到%s成熟了," % self.cook_level)
	
	    def add_cendiments(self, cendiments):
	        self.condiments.append(cendiments)
	
	    def __str__(self):
	        return "牛排已经烤了很久了,现在达到%s成熟了,添加的佐料有%s" % (self.cook_level, self.condiments)
	
	
	hui_ling_dun = CookSteak()
	hui_ling_dun.cook(1)
	hui_ling_dun.cook(1)
	hui_ling_dun.cook(1)
	hui_ling_dun.cook(1)
	hui_ling_dun.add_cendiments("胡椒粉")
	hui_ling_dun.cook(1)
	hui_ling_dun.cook(1)
	hui_ling_dun.add_cendiments("红酒")
	hui_ling_dun.cook(1)
	print(hui_ling_dun)






## 10.17_Python语言基础(访问限制)(掌握)

* 如果有一个对象，当需要对其进行修改属性：
	* 方法2种
	* #直接修改   对象名.属性名 = 数据
	* #间接修改   对象名.方法名（）
#
	 将属性定义为私有
	 格式：
	 __属性名

#### 属性私有案例
#
	# 定义一个类
	class Person(object):
	    def __init__(self, name):
	        self.__name = name
	
	    def __str__(self):
	        return self.__name
	
	    def getName(self):
	        return self.__name
	
	    def setName(self, newName):
	        if len(newName) <= 5:
	            self.__name = newName
	        else:
	            print("名字的长度需要小于等于5")
	
	
	person = Person("张三")
	# print(person)
	# #直接修改   对象名.属性名 = 数据
	# person.__name = "李四"
	# print(person)
	
	# 间接访问   对象名.属性名
	# print(person.__name)  #报错
	
	
	person.setName("李四")
	print(person.getName())
	
	person.setName("王五")
	print(person.getName())


* python没有c++或者Java中的public(公有)  private（私有）区分公有和私有
* python以属性的命名方式来进行区分：
	* 如果在属性名前面加上两个下划线“__”，则表明该属性是私有属性
	* 否则就是公有属性（方法的设置同属性设置一致）
####
	其实，Python并没有真正的私有化支持，但可用下划线得到伪私有。   
	尽量避免定义以下划线开头的变量！
	（1）_xxx      "单下划线 " 开始的成员变量叫做保护变量，
		意思是只有类实例和子类实例能访问到这些变量，
		需通过类提供的接口进行访问；不能用'from module import *'导入
	（2）__xxx    类中的私有变量/方法名 （Python的函数也是对象，
		所以成员方法称为成员变量也行得通。）,
		" 双下划线 " 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。
	（3）__xxx__ 系统定义名字，前后均有一个“双下划线” 代表python里特殊方法专用的标识，
		如 __init__（）代表类的构造函数。


## 10.18_Python语言基础(set()和get()方法)(掌握)
* Python私有属性修改
	* 类中的属性私有化之后,外部无法访问
	* 我们可以在类中定义公共的方法提供给外部,让这个公共的方在类内部修改私有属性
#### set()和get()使用案例:
#
	class Person(object):
	    def __init__(self,name,age,height,weight,money):
	        self.name = name
	        self.__age__ = age
	        self.height = height
	        self.weight = weight
	        self.__money = money
	
	    def ss(self):
	        print(self.__money)
	
	    #通过内部的方法，去修改私有属性
	    #通过自定义的方法实现对私有属性的修改
	    def getMoney(self):
	        return self.__money
	    def setMoney(self,money):
	        #数据的过滤
	        if money < 0:
	            money = 0
	        self.__money = money

	#创建对象
	person = Person("张三",12,170,55,100)
	# person.age = 15
	# person.setMoney(200)
	# print(person.getMoney())
	
	# print(person.__money)#外部使用  不ok
	print(person.ss)#内部  ok


>思考，不能通过对象访问私有属性？
   在python的解释器把__money 变成_Person_money. 
   任然可以使用_Person_money去访问，但是不建议这么做，
***

#

	"""
	person._Person__money = 1
	print(person.getMoney())
	
	print(person.__age__)
	"""
	在python中__XXX__，属于特殊的变量，可以直接访问（公有）
	"""



## 10.19_Python语言基础(复习今天的内容)(掌握)

