## 08.01_Python语言基础(模块概述)(掌握)
#### 模块概述
	在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越难以维护
	为了编写可维护性的代码，我们会把很多函数进行分组，分别放到不同的文件里，
	这样，每个文件包含的代码就相对较少，大多数编程语言都是采用这种组织代码的方式。
	在python中，一个.py文件就称之为一个模块(module)
	模块就好比一个工具包，要想使用这个工具包中的工具（函数），需要导入这个模块
#### 模块优点：
#
	1.提高代码的可维护性
	2.提高代码的复用性，当一个模块定义完毕，可以被多个地方引用
	3.引用其他的模块（内置模块，第三方模块）
	注意：
	   避免函数名和变量名的冲突

## 08.02_Python语言基础(导入模块--import)(掌握)
### 在python中用关键字import来引入模块，一般放在代码最前面
#
	格式：
	  import module1,module2....
  
* 当解释器遇到import 语句，如果模块在当前的搜索路径就会被导入
#
	模块调用函数的基本格式：
	    模块名.函数名（）


#
 	思考：
    为什么必须加上模块名才能调用？
    
    在多个模块中含有同名的函数，此时如果只是通过函数名来进行调用，解释器就无法知道到底需要调用哪个函数
    如果使用import导入模块，在调用的时候必须加上模块名
	import math
	print(sqrt(2))#错误的
	print(math.sqrt(2))
   



### 使用from...import，可以只导入模块的一部分

* 只需要用到模块中的某一个函数，此时只需要引入该函数即可，无需引入模块中的所有函数，浪费内存
#
	格式：
   	from 模块名 import 函数名1，函数名2.....
   
   	案例：
	from  math import sin,cos
	# math.sin()#报错
	sin()
	cos()
	# sqrt()#报错
#
	思考：
	   如果想要引入一个math模块中所有的函数
	   # from math import *




### 使用from...import * 导入模块所有的内容

#
	from...import*：
	把一个模块中所有的内容导入到当前的命名空间
	格式：
	   from  module import *
   



## 08.03_Python语言基础(模块重命名import...as)(掌握)


* as 理解为重命名，将原有的名称替换成一个新的名字

* 作用：
   	有时候导入的模块的名字很长或者很难记住简洁
#
	格式：
	import modName as newName
	   import math as aa(#aa表示math)
	import math as aa
	math#报错
	aa.sin()
	aa.ceil()

#### 注意：如果使用as将原有的模块名重命名，原先的将不可用





## 08.04_Python语言基础(定位模块--搜索路径)(了解)
#
	当你导入一个模块，python的解释器对模块位置的搜索的顺序：
	*	当前目录
	*	如果不再当前的目录，python则搜索在shell变量的PYTHONPATH的每一个目录
	*	模块的搜索路径存储在system模块的sys.path模块中变量，变量中包含当前的目录
	python path和由安装过程决定的默认的目录

pythonpath 变量----》环境变量








## 08.05_Python语言基础(标准函数库中的模块)(熟练)


* math
* random,
* os
* 其他python中自带的标准函数库中的模块





## 08.06_Python语言基础(使用自定义模块)(重点)
### 有些时候，Python自带的模块不能很好的解决我们遇到的问题，我们需要自定义一些具有独特功能的模块来完成代码的编写
#
	"""
	求和函数
	需要传递两个参数：
	a：int
	b : int
	返回a+b的和的结果
	"""
	def add(a,b):
	    return a + b
    





## 08.07_Python语言基础(调用自定义模块)(掌握)
#
	
	import test
	test.add(1,2）

	
### 测试模块

#
	"""
	求和函数
	需要传递两个参数：
	a：int
	b : int
	返回a+b的和的结果
	"""
	
	def add(a,b):
	    return a - b
	
	ret = add(1,-0)
	print(ret)


>为了解决测试的问题，python在执行一个文件时有个变量__name__
如果直接在test.py模块中可以将print进行修改
print()

#
	if __name__ == "__main__":
	     执行语句


## 08.08_Python语言基础(包)(掌握)

* 定义：
   	* 包-----》python中的python package------>文件夹----》容器
* 问题1：
	* 为什么需要引入包？
   	* 将有练习的模块放到一起（便于查找归纳整理）
* 问题2：
    * 如何将有关系的模块联系到一起----》将其放入同一个文件夹
* 问题3：
   	* 放入到同一个文件夹后如何去导入？
   
# 
	  方式1：
	  使用import关键字导入
	  格式：
		import 文件.模块
		import day09.test
		# day09.test.add(1,2)
		day09.test.add(1,2)
#
	方式2：
		使用from 文件夹 import 模块
		格式：
	    from 文件夹的名字 import 文件名
    
		from day09 import test

		test.add(1,2)
包使用总结：
#
	总结：
	   包将有联系的模块组织在一起，放到同一个文件夹下，
	在创建文件夹的时候会自动创建一个__init__.py文件，======》包
想一想
#
	1. __init__.py文件有什么用？
	   __init__.py控制着包的导入的行为
	2.__init__.py文件为空？
	仅仅是把包导入，不会导入该包中的模块



 


## 08.09_Python语言基础(安装第三方模块)(掌握)
* https://pypi.org/
* 不同系统的安装方式：
	* mac-------》无需安装
	* Linux------》无需安装
	* Windows--》pip
* 比如：pygame   非常强大的游戏开发库
#
	格式：
	  打开命令提示符
	  DOS命令
	  pip install 第三方的模块名（前提都是要求联网下载）

pip的安装：
#
	pip的安装：
	1.到https://pypi.python.org/pypi/pip   下载pip版本tar.gz,下载完成直接到本地解压
	2.在DOS命令行进入pip解压的目录，输入python setup.py install进行安装
	3.如果安装完成  提示finished   
	4.如果出现问题提示pip没有找到该命令，可以将python/Script目录配置到path环境变量中

安装PTL


## 08.10_Python语言基础(时间相关的模块)(熟练)

* time 
	* import time
####
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
* datetime  	
	* import datetime
* calendar
	* import calendar
* python时间分类
	* 浮点型
		* time.time()/mktime()...
	* 字符串
		* time.asctime()/time.ctime()...
	* 元组
		* time.localtime()/time.gttime()


### 在python中表示时间的方式：
#
	时间戳（timestamp）:
		时间戳表示的是从1970年1月1日00:00:00，按秒计算偏移量
		time()
	
	print(type(time.time()))	#返回的是float
	print(time.time())


### 格式化的时间字符串(了解)：
#
	%a	本地简化的星期的名称
	%A	完整的星期的名称
	%b	简化的月份的名称
	%B	完整的月份的名称
	%c	本地对应的日期表示和时间表示
	%d	月内中的天数（0~31）
	%H	24小时制小时数（0~23）
	%m	月份（01~12）
	%M	分钟数（00~59）
	%w	星期（0~6） 星期天开始



元组：共有9中元素，返回的是struct_time的函数主要有gmtime(),localtime(),strptime()
#
	索引   属性         	值
	0     tm_year(年)      2018
	1     tm_mon(月)       1~12
	2     tm_mday(日)      0~31
	3     tm_hour(时)      0~23
	4     tm_min(分钟)     0~59
	5     tm_sec(秒)       0~61
	6     tm_wday(weekday)   0~6(0表示周日) 
	7     tm_yday(一年中的第几天)   1~366
	8     tm_isdst(是否是夏令时)   默认为-1
	
	import time
	t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
	t = time.mktime(t)
	print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

	UTC :世界协调时间  格林威治天文时间  世界标准时间
		 在中国UTC+8

	#localtime():获取当前时间，返回struct_time格式返回
	#获取当前的时间

	# print(time.localtime())
	
* 时间的相关操作
* 类型转换
	* 浮点型--》字符串
		* time.ctime(time.time())
	* 字符串--》浮点型
		* time.mktime(time())


	* 字符串--》元组
		* time.asctime(time.localtime())
	* 元组--》字符串
		* time.asctime(time.localtime())
	

	* 浮点型--》元组
		* time.localtime(time.time())
	* 元组--》浮点型
		* time.mktime(time.localtime())

* 格式化时间
	* 格式化成2019-03-20 11:45:39形式
		* print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	
	* 格式化成Sat Mar 28 22:24:24 2019形式
		* print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
	
	* 将格式字符串转换为时间戳
		* a = "Sat Mar 28 22:24:24 2019"
		* print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

### 获取当天的时间和日期
#
	# 获取当天的时间
	print(datetime.datetime.now())
	# 当前的日期
	print(datetime.date.today())


	# 获取昨天的时间
	def getYesterday():
	    today = datetime.date.today()
	    oneday = datetime.timedelta(days=1)
	    yesterday = today - oneday
	    print(type(today))
	    print(type(yesterday))
	    return yesterday
	yesterday = getYesterday()
	print(yesterday)

	#获取日历相关的信息
	
	#获取某个月的日历
	# 格式：calendar.month(x,y)x:显示的年份，y
	# 显示的月份
	cal = calendar.month(2015,12)
	print(cal)
	#设置日历的第一天
	calendar.setfirstweekday(calendar.SUNDAY)
	cal = calendar.month(2015,12)
	print(cal)
	
	#获取某一年的日历：
	cal = calendar.calendar(2015)#参数为具体的年份
	print(cal)
	cal = calendar.HTMLCalendar(calendar.MONDAY)
	print(cal.formatmonth(2015,12))


## 08.11_Python语言基础(collections--集合相关模块)(熟练)
* collections
	* python内建的一个集合模块，提供了许多有用的集合类
* nametuple
	* Returns a new subclass of tuple with named fields.
	* 命名元组，本质是一个函数，用它来创建一个自定义的tuple对象
	* 规定tuple元素的个数，并可以用属性而不是索来引用tuple中的元素
	* 用namedtuple定义一个新的数据类型
### nametuple案例
	#定义了一个新的数据类型，属于tuple类型的子类型
	Point = namedtuple("Point", ["x", "y"])
	print(Point)
	print(Point.__name__)
	point = Point(1, 2)
	print(isinstance(point, tuple))
	print(isinstance(point, Point))
	print(point)
	print(point[0], point[1])
	# 根据属性获取值
	print(point.x, point.y)

* deque
	* deque([iterable[, maxlen]]) --> deque object
	* A list-like sequence optimized for data accesses near its endpoints.
	* collections模块中的一个类
	* 类似list，优化了一些列表的操作，提高了操作列表数据的效率
	* list存储数据，按索引访问元素，但是插入和删除元素会根据元素的个数增多而效率降低
	* list是线性存储，数据量大插入和删除效率会低
### deque案例
	q = deque([1,2,3,4,5])
	
	q.append(6)
	q.appendleft(0)
	q.pop()
	q.popleft()
	print(q)
	print(type(ret))
	print(isinstance(ret, list))
	print(list(ret))
	print(isinstance(ret, Iterable))
	print(isinstance(ret, Iterator))