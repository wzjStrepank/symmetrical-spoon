## 12.01_Python语言基础(类对象)(掌握)
### python中的类,类同样也是一种对象,这个对象使用关键字class
### python解释器在执行的时候会创建一个对象
### objectCreater
#
	class Test(object):
	    pass
	
	test = Test()
	print(test)#结果为类创建对象在内存中的地址
#### 判断一个对象是否在某个类中--hasattr(obj,str)
#
	class Test(object):
	    pass
	
	test = Test()
	print(test)
	print(Test)
	
	def info(o):
	    print(o)
	#可以将类作为参数传递函数
	info(test)
	#可以为类添加新的的属性
	print(hasattr(Test,"new_attribute"))
	Test.new_attribute = "haha"
	print(hasattr(Test,"new_attribute"))
	print(Test.new_attribute)
	
	#将一个类赋值给一个变量
	test1 = Test
	print(test1)






## 12.02_Python语言基础(动态创建类)(掌握)

#### 动态创建类
	def choose_name(name):
	    if name == "haha":
	        class haha(object):
	            pass
	        return haha
	    else:
	        class heihei(object):
	            pass
	        return heihei


	myClass = choose_name("haha")
	print(myClass)#函数返回的haha --->  类,不是类的实例
	print(myClass())#返回类创建的实例,也是对象


>python中的内建函数type()--》查看对象所属的类型，作用和__class__类似


#
	print(type(1))
	print(type("1"))
	print(type(choose_name("haha")))#类的类型  返回值-->type





## 12.03_Python语言基础(type创建类)(掌握)

* 动态创建类
	* 格式：
		* type(类名，由父类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
#### type创建类案例：

#
	Test01 = type("Test01", (), {})	
	print(Test01)
	print(Test01())	

	输出结果：
	<class '__main__.Test00'>
	<__main__.Test00 object at 0x000001360A04C160>

>结果：显示和我们学习的类具有一样类型的内存地址







## 12.04_Python语言基础(使用type函数创建带有属性的类)(掌握)

* type接受一个字典来定义类的属性
* type("类名"，(),{"name":"zhangsan"})
#### type创建有内容的类
#
	Test01 = type("Test01", (), {"name": "hello", "age": 18})
	print(Test01)
	print(Test01())
	print(Test01().name)
	print(Test01().age)

	输出结果：
	<class '__main__.Test01'>
	<__main__.Test01 object at 0x0000025B5773B860>
	hello
	18





## 12.05_Python语言基础(type创建带有继承关系的类)(掌握)
#
	Test01 = type("Test01", (), {"name": "hello", "age": 18})
	print(Test01)
	print(Test01())
	print(Test01().name)
	print(Test01().age)
	

	Test02 = type("Test02", (Test01,), {})
	print(Test02)
	print(Test02())
	print(Test02.__mro__)

	输出结果：
	<class '__main__.Test02'>
	<__main__.Test02 object at 0x000002BBD33FBA58>
	(<class '__main__.Test02'>, <class '__main__.Test01'>, <class 'object'>)

>**注意：**<br/>
    type函数中有三个参数，字符串是类名，元祖中是父类的名字，字典中添加属性<br/>
    添加的属性是类属性，不是实例属性，类对象和实例对象都能调用<br/>
	添加的方法可以是普通方法，静态方法，类方法<br/>
***




## 12.06_Python语言基础(type动态创建带方法的类)(掌握)

#### type添加实例方法

#
	1,添加实例方法
	Test01 = type("Test01", (), {"name": "hello", "age": 18})
	print(Test01)
	print(Test01())
	print(Test01().name)
	print(Test01().age)
	
	
	def test(self):
	    print("haha")
	
	
	Test02 = type("Test02", (Test01,), {"test": test})
	print(Test02)
	print(Test02())
	print(Test02().test)
	# demo02 = Test02().
	Test02().test()
	print(Test02.__mro__)



#### type添加一个静态方法和类方法

#
	1，添加静态方法
	@staticmethod
	def test03():
	    print("hahaha--test03")
	    return "test03"
	
	
	Test003 = type("Test003", (Test01,), {"test03": test03})
	print(Test003)
	print(Test003().test03())
	
	2，添加类方法
	@classmethod
	def test04(cls):
	    print("hahaha--test04")
	    return "test04"
	
	
	Test004 = type("Test004", (Test01,), {"test04": test04})
	print(Test004)
	print(Test004().test04())

>**总结:**<br/>
元类是创建类所需要的类，创建类就是为了创建类的实例对象<br/>
python中类也是对象<br/>
元类：就是用来创建这些类（对象）的类----》元类<br/>
myclass = type(name,(),{})#使用元类创建一个对象，这个对象称之为类<br/>
myobject = myclass()#使用类创建类的实例对象<br/>
type实际上就是一个元类，是python在幕后创建所有类的元类<br/>
***






## 12.07_Python语言基础(__class__)(掌握)
#### __class__可以查看元素、对象所属的类，功能和type相似

#
	print("-" * 30)
	age = 35
	print(age.__class__)
	name = "zhangsan"
	print(name.__class__)
	
	
	def test():
	    pass
	
	
	print(test.__class__)  # function
	
	
	class demo:
	    pass
	
	
	print(demo.__class__)  # type
	
	print(age.__class__.__class__)  # type
	print(name.__class__.__class__)
	
	输出结果：
	------------------------------
	<class 'int'>
	<class 'str'>
	<class 'function'>
	<class 'type'>
	<class 'type'>
	<class 'type'>

	


## 12.08_Python语言基础(python是动态语言)(掌握)
#### 动态语言的定义
* 变量可以任意更改，不用考虑类型
* 类可以当做参数传递
* 方法，函数可以动态添加到类中
* 属性可以动态添加到类中
* 。。。 。。。 


#### 运行中给对象绑定（添加属性） 

#
	class Person(object):
	    def __init__(self, name=None, age=None):
	        self.name = name
	        self.age = age
	
	
	P = Person("小明", "22")
	P.sex = "male"
	print(P.sex)

	输出结果：
	male

#### 运行的过程中给类绑定属性

#
	class Person(object):
	
	    def __init__(self, name=None, age=None):
	        self.name = name
	        self.age = age
	
	
	p = Person("小丽", "23")
	Person.sex = None
	print(p.sex)


> **总结:**<br/>
运行中给对象绑定属性-----》直接通过实例对象设置<br/>
运行中给类绑定属性-----》直接通过类对象设置<br/>
***





## 12.09_Python语言基础(运行中给类绑定方法)(熟练)
####使用type动态添加方法
#
	print("-" * 30)
	
	class Person(object):
	    def __init__(self, name=None, age=None):
	        self.name = name
	        self.age = age
	
	    def eat(self):
	        print("吃饭....")
	
	def run(self, speed):
	    print("%s在移动,速度%s" % (self.name, speed))

	p = Person("老王", 23)
	p.eat()
	
	# p.run()
	person = type("person", (Person,), {"run": run})
	P = person("小王", "24")
	P.run("220")

	输出结果：
	------------------------------
	吃饭....
	小王在移动,速度220

#### 使用types动态添加方法
	print("*" * 30)
	
	import types

	class Person(object):
	    def __init__(self, name=None, age=None):
	        self.name = name
	        self.age = age
	
	    def eat(self):
	        print("吃饭....")

	def run(self, speed):
	    print("%s在移动,速度%s" % (self.name, speed))
	
	P = Person("小王","24")
	# P.run("220")
	
	P.run = types.MethodType(run,P)#第一个参数L:需要添加的方法,参数二:添加到该类的实例对象
	P.run("100")

	运行结果：
	******************************
	小王在移动,速度100

#### 动态添加一个静态方法
#	
	# 定义一个类方法
	@classmethod
	def testClass(cls):
	    cls.num = 150
	
	
	# 定义一个静态方法
	@staticmethod
	def testStatic():
	    print("----static method-----")
	P = Person("老王",22)
	Person.testClass = testClass    # 把静态方法加入到类中
	Person.testClass()              # 调用类的静态方法,执行方法中的方法体
	print(Person.num)               # 输出调用内容
	
	print("$" * 30)
	# 添加静态方法
	Person.testStatic = testStatic
	Person.testStatic()
	
	输出结果:
	******************************
	150
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	----static method-----





## 12.10_Python语言基础(运行过程中删除属性和方法)(熟练)


* 删除的方法:
   * del  对象.属性名
   * delattr(对象,"属性名")





## 12.11_Python语言基础(@property)(掌握)

### 私有的属性添加给getter和setter

#
	class Money(object):
	    def __init__(self):
	        self.__money = 0
	
	    def getMoney(self):
	        return self.__money
	
	    def setMoney(self, value):
	        if isinstance(value, int):
	            self.__money = value
	        else:
	            print("error:不是整型")
		# 先后调用两个方法,调用set方法的值,通过set设置
	    money = property(getMoney, setMoney)  

	
	a = Money()
	print(a.money)
	a.money = 100
	print(a.money)
	
	print(a.getMoney())


#### 使用property实现getter 和 setter方法的功能

#
	如何实现set/get------》修饰器-----》@property
	@property--->属性函数，可以对属性赋值时候做必要的检查，并保证代码的原有功能
	作用：
	1.将方法转化为只读
	2.重新实现一个属性的设置和读取方法，可做边界判定

	class Money:
	    def __init__(self):
	        self.__money = 0
	
	    @property
	    def money(self):
	        return self.__money
	
	    @money.setter
	    def money(self, value):
	        if isinstance(value, int):
	            self.__money = value
	        else:
	            print("error....")
	
	
	a = Money()
	print(a.money)
	a.money = 189
	print(a.money)

#### 案例2:
#
	#使用set和get方法
	class Person(object):
	    def __init__(self,name,age):
	        #属性直接对外暴露
	        # self.age = 12
	        #限制属性
	        self.__name = name
	        self.__age = age
	    def getAge(self):
	        return self.__age
	    def setAge(self,age):
	        if age < 0:
	            age = 0
	        self.__age = age

	# 使用修饰器实现set和get功能
	print("*" * 30)
	
	
	class Person:
	    def __init__(self):
	        self.__name = "oo"
	        self.__age = 34
	
	    @property
	    def age(self):
	        return self.__age
	
	    @age.setter
	    def age(self, age):
	        if age > 0 and age < 100:
	            self.__age = age
	
	
	p = Person()
	print(p.age)




## 12.12_Python语言基础(运算符的重载)(掌握)
* 同样的运算符执行不同数据之间的运算时，采用不同的计算方式
#### 运算符的重载案例1：
#
	print(1+2)
	print("1"+"2")
#### 案例2:
#
	class Person(object):
	    def __init__(self,num):
	        self.num = num
	
	    #运算符重载
	    def __add__(self, other):
	        return Person(self.num+other.num)

	    def __str__(self):
	        return "num="+str(self.num)
	per1 = Person(1)
	per2 = Person(2)
	print(per1+per2)#3  ====print(per1.__add__(per2))
	print(per1.__add__(per2))
	print(per1)
	print(per2)


>不同的类型数据用加法会有不同的解释
***


## 12.13_Python语言基础(发邮件)(了解)
#
	SMTP是SIMPLE MAIL TRANSFER PROTOCOL的缩写，
	一般的发信软件，如Outlook Express、FoxMail、Eudora都是使用这个协议进行发信的。
	SMTP Host 中文意思就是"简单邮件传送协议服务器"
	一般免费的邮箱,如下列出的,他们的SMTP服务器就是在域名前加上smtp就行了.
	smtp.163.com
	smtp.21cn.com
	smtp.sina.com.cn
	smtp.sohu.com
	smtp.126.com
	对应的别一个邮件协议是:POP3(Post Office Protocol 3)。
	它规定怎样将个人计算机连接到Internet的邮件服务器和下载电子邮件的电子协议。
	它是因特网电子邮件的第一个离线协议标准,POP3允许用户从服务器上把邮件存储到本地
	主机（即自己的计算机）上,同时删除保存在邮件服务器上的邮件，
	而POP3服务器则是遵循POP3协议的接收邮件服务器，用来接收电子邮件的。

#### 乞丐版
#
	from email.mime.text import MIMEText
	import smtplib

	msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
	
	# 输入Email地址和口令:
	from_addr = "dusine@126.com"
	password = "XXXXXX"
	# 输入SMTP服务器地址:
	smtp_server = "smtp.126.com"
	# 输入收件人地址:
	to_addr = "dujunqiang@xxxxx.com"
	
	server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
#### 精装版
# 

## 12.14_Python语言基础(发送短信)(了解)
#### 使用亿信互联
#
	# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
	# 账户注册：请通过该地址开通账户http://user.ihuyi.com/register.html
	# 注意事项：
	# （1）调试期间，请使用用系统默认的短信内容：您的验证码是：【变量】。请不要把验证码泄露给其他人。
	# （2）请使用 APIID 及 APIKEY来调用接口，可在会员中心获取；
	# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
	
	# !/usr/local/bin/python
	# -*- coding:utf-8 -*-
	import http.client
	import urllib.parse
	
	host = "106.ihuyi.com"
	sms_send_uri = "/webservice/sms.php?method=Submit"
	
	# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
	account = "C45031386"
	# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
	password = "481af8a3a877b0275d0adb91d0d7fdae"
	
	
	def send_sms(text, mobile):
	    # 参数
	    params = urllib.parse.urlencode(
	        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
	    # 请求头
	    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	    # 链接目标
	    conn = http.client.HTTPConnection(host, port=80, timeout=30)
	    # 发起请求
	    conn.request("POST", sms_send_uri, params, headers)
	    # 获取响应
	    response = conn.getresponse()
	    # 获取响应内容
	    response_str = response.read()
	    # 关闭连接
	    conn.close()
	    # 把结果返回给调用者
	    return response_str
	
	
	if __name__ == '__main__':
	    # 手机号码
	    mobile = "1897012800"
	    # 发送的验证码内容
	    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"
	
	    print(send_sms(text, mobile))

