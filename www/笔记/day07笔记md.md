## 07.01_Python语言基础变量(Python变量)(重点重点重点掌握)
### 变量的分类
	* 局部变量
	* 成员变量（全局变量）


### 局部变量

#
	#局部变量
	def test1():
	    a = 10
	    b = 10
	    
	def test2():
	    a = 10
	    b = 20
	    
	# 以上函数中的变量----》局部变量
#
	总结：
	局部变量：
	    就是在函数内部定义的变量
	    不同的函数，可以定义相同名字的局部变量，各个变量之间不会发生干涉不会影响
	    局部变量的作用：为了临时保存数据需要在函数中定义变量来进行保存


### 全局变量
#	
	#全局变量
	
	定义：
	   如果一个变量，既能在一个函数中使用，
	 也能在另外一个函数中使用---》全局变量
	"""
	#定义一个全局变量
	a = 100
	def test3():
	    print(a)
	def test4():
	    print(a)
	
	test3()
	test4()


	


### 全局变量和局部变量名字相同的问题
#	
	"""
	全局变量和局部变量名字相同的问题
	"""  
	s = 100
	def test5():
	    s = 200
	    print(s)
	    s = 300
	    print(s)
	    
	def test6():
	    print(s)
	test5()

### 修改全局变量

	* global  关键字   修改全局变量

	* 格式：global 需要修改变量名  
#
	# 没有加global修饰的全局变量
	num = 11
	def num01():
	    num = 12
	    return num
	print(num01())
	print(num)
	print("*" * 30)

	# 在外部加global修饰的全局变量
	global num001
	num001 = 110
	def num011():
	    global num001
	    num001 = 100
	    return num001
	print(num011())
	print(num001)
	print("*" * 30)

	# 在函数内部加global修饰的全局变量
	num002 = 110
	def num012():
	    global num002
	    num002 = 100
	    return num002
	print(num012())
	print(num002)
	print("*" * 30)



再来一个案例
#
	print("*" * 30)

	wendu = 0
	def get_wendu():
		# 想一下wendu=33不加注释的运行结果
	    # wendu = 33
	    global wendu
	    wendu = 34
	
	def print_wendu():
	    print(wendu)
	
	get_wendu()
	print_wendu()

### 局部变量和全局变量的区别

#
	1.在函数外面定义的变量称为：全局变量
	2.全局变量能够在所有的函数中被访问
	3.如果在函数中修改全局变量，那么需要使用global关键字进行声明，否则出错
	4.如果出现同名的现象，先到局部找---》全局-----》报错，这个被称为：就近原则

	他们的本质的区别：
	     在于作用域

局部变量和全局变量区别案例
#	
	#案例：
	def get_wendu():
	    wendu = 33
	    return wendu
	def print_wendu(wendu):
	    print(wendu)
	    
	result = get_wendu()
	print_wendu(result)
	
	wendu = 0
	def get_wendu1():
	    wendu = 34
	    # global wendu
	    wendu = 33
	    
	def print_wendu1():
	    print(wendu)


### 可变类型的全局变量


* 可变类型值:   列表   字典   集合
* 不可变类型:   引用   元祖   数字  字符串

#
	当不可变的数据类型作为全局变量： 需要用global声明，进行修改
	当可变的数据类型作为全局变量：  不一定需要global声明


### 可变类型的全局变量案例：
#
	#案例：
	test = []
	def d():
	    test.append(2)
	    print(test)
	d()
	
	test1 = []
	def e():
	    test1 = [1,2]
	    # global test1
	    test1 = [3,4]
	    # print(test1)
	e()
	print(test1)
	
	test2 = [1,2]
	def f(a):
	    a += a
	    print(a)
	
	f(test2)
	print(test2)

再来一个案例
#
	# 没有加global修饰的全局变量--可变类型
	list01 = [1, 2, 3, 4]
	def list001():
	    list01.append(5)
	    return list01
	print(list001())
	print(list01)
	print("*" * 30)

	# 加global修饰的全局变量--可变类型
	global list02
	list02 = [6, 1, 2, 3, 4]
	def list002():
	    global list02
	    list02.append(5)
	    return list02
	print(list002())
	print(list02)

### 不可变类型的全局变量案例：
#
	#不可变
	a = 1
	def g():
	    a = 2
	    a += 1
	    print(a)
	    # global a
	    a = 4
	g()
	print(a)

·
## 07.02_Python语言基础(生成器)(熟练)
* Python的生成器是一个返回可以迭代对象的函数。
* 先看案例：
创建一个列表，元素为0--20以内的偶数
#
	list01 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
	list02 = [x * 2 for x in range(1, 10)]
	Generator01 = (x * 2 for x in range(1, 10))
	print(list01)
	print(list02)
	print(Generator01)
	for i in Generator01:
	    print(i, end=",")
运行输出结果：
#
	[2, 4, 6, 8, 10, 12, 14, 16, 18]
	[2, 4, 6, 8, 10, 12, 14, 16, 18]
	<generator object <genexpr> at 0x0000014043D37200>
	2,4,6,8,10,12,14,16,18,

* 创建生成器的方式有多种，只要把一个列表生成式的[]改成()
* 创建list和Generator区别在于外层[],(),list表示一个列表，Generator表示生成器
* 遍历生成器内容：
	* next()
	* for循环
	
next()读取生成器内容
#
	# next
	# 定义一个生成器
	Generator = (x * 2 for x in range(5))
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	temp = next(Generator)
	print(temp)
	
	temp = next(Generator)# 注意:如果一直写next()函数,当超出了元素的个数范围的时候会直接报错
	print(temp)
运行输出结果：
#
	0
	2
	4
	6
	8
	Traceback (most recent call last):
	  File "/Day06/Generator_Demo01.py", line 24, in <module>
    temp = next(Generator)
	StopIteration

for循环遍历生成器内容：
#
	# 循环遍历
	Generator = (x*2 for x in range(5))
	for temp in Generator:
	    print(temp)
运行输出结果：
#
	0
	2
	4
	6
	8
>读取到最后一个元素自动结束，不会报错

#
	总结:
	生成器保存的是一个算法,每次调用next()函数,就能计算出生成器下一个元素的值,直到最后一个元素，
	如果超出了元素的最大长度范围,报错,
	通过for循环来迭代他,并且不用关心超出界限的问题



## 07.03_Python语言基础(函数实现生成器)(掌握)
* 函数来实现生成器(函数后面学习)
#
	函数的定义:
	格式: def 函数名():
		方法体语句

	函数的调用:函数名()

* 练习:菲波拉锲数列
#
	1 1 2 3 5 8 13    除第一个和第二个外,任意的数都是由前两个数相加得到

	a = 0
	b = 0
	c = 1
	while a < 5:
	    temp = c
	    c = b + c
	    b = temp
     	a += 1
	    print(b)


* 函数（方式一）
#
	def fib1():
	    a = 0
	    b = 0
	    c = 1
	    while a < 5:
	        temp = c
	        c = b + c
	        b = temp
	        a += 1
	        print(b)
	fib1()


* 函数（方式二）
#
	def fib2():
    	a = 0
    	b,c = 0,1
    	while a < 5:
	        print(c)
	        b, c = c , b + c
	        # b = c
	        # c = b + c
	        a += 1

	fib2()
解释一下代码：
#
	a = 0
	b = 1
	a,b = b, a + b
	相当于
	temp = b
	b = a + b
	a = temp
	
	或者:
	   a, b = b , a + b 


## 07.04_Python语言基础(生成器--yield)(掌握)
* 先看代码：
#
	print("-----fib3()---------")
	def fib3():
	    a = 0
	    b, c = 0, 1
	    while a < 5:
	        # print(c)
	        yield c
	        b, c = c, b + c
	        a += 1

	f = fib3()#生成器
	print(f)
	print(next(f))
	print(next(f))
	print(next(f))
	print(next(f))
	print(next(f))
运行输出结果：
#
	-----fib3()---------
	<generator object fib3 at 0x000002352A007360>
	1
	1
	2
	3
	5
* yield是一个类似return的关键字,迭代一次遇到yield的时候返回(右侧,后面的值)
* 重点:
	* 下一次迭代时,从上一次迭代遇到yield后面的代码(下一行)开始执行
		* return返回一个值,并且记住返回值的位置,
    	* 下次迭代的时候就从这个记录的位置开始
	* 输出时注意调用next()的次数，超出内容会报错



## 07.05_Python语言基础(迭代器概述)(掌握)
* 迭代：
   * 迭代是重复反馈过程的活动，其目的通常是为了逼近所需目标或结果。
   * 每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。
   * 计算机中的迭代：对计算机特定程序中需要反复执行的子程序*(一组指令)，进行一次重复，即重复执行程序中的循环，直到满足某条件为止，亦称为迭代
   * Python中的迭代是访问集合元素的一种方式
* 迭代器：
   * 可以被next()函数调用并且不断的返回下一个值的对象(迭代器 Iterator)
* 可迭代对象：
   * 是一个可以记住遍历位置的对象
   * 迭代器对象从集合的第一个元素开始访问，直到所有的元素访问完毕为止
* 迭代器的特点：
  * 只能往前，不会后退


## 07.06_Python语言基础(可迭代对象)(掌握)
* 直接可用for循环遍历的数据类型有哪些？
	* 一类：list  tuple  dict  set  str
	* 一类：生成器
* 这些可以直接作用与for循环的对象的统称----》可迭代对象（Iterable）
* **怎么判断是否可以迭代？**
	* 可以使用isinstance()来判断一个对象是否是Iterable，返回值是True或者False
	* 需要使用一个模块collections

#
	from collections import Iterable
	a = isinstance([],Iterable)
	b = isinstance((),Iterable)
	c = isinstance({},Iterable)
	d = isinstance("aaaa",Iterable)
	e = isinstance(1000,Iterable)#false
	f = isinstance((x for x in range(5)),Iterable)
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
	print(f)
运行输出结果：
#
	True
	True
	True
	True
	False
	True


## 07.07_Python语言基础(迭代器)(掌握)
* 迭代器：
   * 可以被next()函数调用并且不断的返回下一个值的对象(迭代器 Iterator)
* 判断一个元素是不是迭代器：isinstance（ocject, Iterator）
#
	print("--------Iterator---------")
	from collections import Iterator
	
	a = isinstance([], Iterator)
	b = isinstance((), Iterator)
	c = isinstance({}, Iterator)
	d = isinstance("aaaa", Iterator)
	e = isinstance(1000, Iterator)
	f = isinstance((x for x in range(5)), Iterator)
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
	print(f)

	运行输出结果：
	
	--------Iterator---------
	False
	False
	False
	False
	False
	True

#
	Python中 list、truple、str、dict这些都可以被迭代，但他们并不是迭代器。为什么？

	因为和迭代器相比有一个很大的不同，list、truple、map、dict这些数据的大小是确定的，
	也就是说有多少事可知的。
	但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，
	每调用一次next()，就会往下走一步，是惰性的。

	判断是不是可以迭代，用Iterable
	判断是不是迭代器，用Iterator

	所以，
	凡是可以for循环的，都是Iterable
	凡是可以next()的，都是Iterator

	集合数据类型如list、truple、dict、str都是Itrable不是Iterator，
	但可以通过iter()函数获得一个Iterator对象

	Python中的for循环就是通过next实现的
 


## 07.08_Python语言基础(Iter()函数)(掌握)
* 生成器都是Iterator对象，但是list、dict、str都是迭代对象但是不是迭代器
* 使用iter()函数可以把这些可迭代对象转换为迭代器
案例代码：
#
	print("-----------Iter()-------------")
	from collections import Iterator
	
	words = [1, 5, 8, 3, 5]
	a = isinstance(iter(words), Iterator)
	b = isinstance(iter(()), Iterator)
	c = isinstance(iter({}), Iterator)
	d = isinstance(iter("hhaha"), Iterator)
	f = isinstance((x for x in range(5)), Iterator)
	print(a)
	print(b)
	print(c)
	print(d)
	print(f)
	
	words = iter(words)
	print(next(iter(words)))
	print(next(iter(words)))
	print(next(iter(words)))
运行输出结果：
#
	-----------Iter()-------------
	True
	True
	True
	True
	True
	1
	5
	8



## 07.09_Python语言基础(迭代器总结)(掌握)
#
	1.凡是可以作用与for循环对象都是Iterable类型
	2.可以作用与next()函数的对象都是Iterator类型
	3.集合数据类型list、tuple、dict、str等是Iterable但不是Iterator
	4.集合数据类型list、tuple、dict、str等通过iter()可以将其转换为Iterator


## 07.10_Python语言基础(递归函数)(重点)

### 递归函数的定义

#
	定义：
		在函数中不调用其他函数，而是调用自己------》递归函数（自己玩自己）
		凡是循环能做的事，递归都能做  


### 递归函数的作用
#
	

	   
	def show():
	    print("我叫王二小")
	    show()
	show()
	
	
	"""	
	例如：

	   计算一个阶乘n!
	   n! = 1*2*3*4...*n
	   1! = 1
	   2! = 2*1 2*1!
	   3! = 3*2*1 3*2!
	   4! = 4*3*2*1 4*3!
	   n! = n*(n-1)!
	   
	   参数
	       要   1个   
	   返回值
	       要   结果    

	#方法1
	def calnum(num):
	    # for temp in range(1,num+1):
	    i = 1
	    result = 1
	    while i <= num:
	        # result = result * i
	        result *= i
	        i += 1
	    return result
	ret = calnum(3)
	print(ret)

	#方法2：
	def calnum(num):
	    if num >=1:
	        result = num*calnum(num-1)
	    else:
	        result = 1
	    return result
	ret = calnum(3)
	print(ret)


>注意：防止死循环（递归）

### 递归遍历目录

	import os
	 
	def getAllDirRE(path,sp = ""):
	    #得到当前目录下的所有的文件
	    filesList = os.listdir(path)
	    #处理每一个文件
	    sp += "  "
	    for fileName in filesList:
	        #判断是否是路径（用绝对路径）
	        fileAbsPath = os.path.join(path,fileName)
	        if os.path.isdir(fileAbsPath):
	
	            print(sp+"目录：",fileName)
	            #递归函数
	            getAllDirRE(fileAbsPath,sp)
	        else:
	            print(sp + "普通文件",fileName)
	getAllDirRE(r"G:\1901")


## 07.11_Python语言基础(栈模拟递归遍历目录)(熟练)
* 模拟栈存储方式获取指定路径下所有文件
#
	栈定义：
	    又名堆栈，
	import os
	"""
	栈：
	    先进后出
	    装子弹
	"""
	#模拟栈结构
	#入栈
	stack = []
	stack.append("A")
	print(stack)
	stack.append("B")
	print(stack)
	stack.append("C")
	print(stack)
	
	#出栈
	res1 = stack.pop()
	print("res1=",res1)
	print(stack)
	res2 = stack.pop()
	print("res1=",res2)
	print(stack)

	def getAllDirRE(path):
	    stack = []
	    stack.append(path)
	    #处理栈，当栈为空的时候结束当前动作
	    while len(stack) != 0:
	        #从栈中取数据
	        dirPath = stack.pop()
	        filesList = os.listdir(dirPath)
	        #得到的数据，如果是普通的文件，直接打印，如果，是目录继续压栈
	        for fileName in filesList:
	            fileAbsPath = os.path.join(dirPath,fileName)
	            if os.path.isdir(fileAbsPath):
	                print("目录"+fileName)
	                #压栈
	                stack.append(fileAbsPath)
	            else:
	                print("普通"+fileName)
	getAllDirRE(r"G:\1901")
## 07.12_Python语言基础(队列模拟遍历目录)(熟练)
* 模拟队列获取指定路径下所有文件


#
	"""
	先进先出   排队
	collections
	append:添加
	queue：获取队列
	len:获取长度
	popleft:出队
	
	listdir:获取当前目录的所有文件
	isdir  :判断是否是文件
	
	"""
	import os
	import collections
	
	def getAllDirQu(path):
	    #创建一个队列
	    queue = collections.deque()
	    #进队
	    queue.append(path)
	    while len(queue) != 0:
	        #出队
	        dirPath = queue.popleft()
	        #获取当前路径下的所有的文件
	        filesList = os.listdir(dirPath)
	
	        for fileName in filesList:
	            #绝对路径
	            fileAbsPath = os.path.join(dirPath,fileName)
	            #判断是否是目录（文件夹），如果是进队，不是直接打印
	            if os.path.isdir(fileAbsPath):
	                print("目录："+fileName)
	                queue.append(fileAbsPath)
	            else:
	                print("普通文件"+fileName)
	
	getAllDirQu(r"D:\1901"）


