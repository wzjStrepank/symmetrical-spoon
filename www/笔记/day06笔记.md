## 函数
#### 函数多个返回值
* 多个返回值时返回的是元组
* 

		import math
	
		def get_result(a,b,c):
		    peri = a + b + c
		    p = peri / 2
		    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
		    return peri,area
	
		print(get_result(3,4,5))
		print(type(get_result(3,4,5)))
		===>
		(12, 6.0)
		<class 'tuple'>
#### 函数的嵌套




#### 函数也是一种数据---回调函数
* 回调函数就是一个通过函数指针调用的函数。

* 如果你把函数的指针（地址）作为参数传递给另一个函数，当这个指针被用来调用其所指向的函数时，我们就说这是回调函数。

* 回调函数不是由该函数的实现方直接调用，而是在特定的事件或条件发生时由另外的一方调用的，用于对该事件或条件进行响应。
* 回调函数案例
* 
		def sweep(times):
	   		print("今天扫地%d次" % times)
	
		def mop(times):
		    print("今天拖地%d次" % times)
			
		def change_sheets(times):
		    print("今天换床单%d次" % times)
		
		def callback(func, times):
		    return func(times)
		
		callback(change_sheets, 3)
		# ---》change_sheets(3)
		===>
		今天换床单3次
* 回调函数VS一般函数
	* 回调函数
		* 传入的参数是函数名，和传入函数对应的参数
		* 先返回回调结果，在执行参数函数
	* 普通函数
		* 可以传入普通参数、函数调用
		* 普通函数传入函数调用，执行顺序：先执行最内层的函数，逐层向外执行
* 
		"""
		计算数字字符串的二进制结果
		"""
		
		print(int("110", base=2))
			
		def get_n(num):
		    return num * 2 - 1		
		
		def get_bin(num):
		    return int(num, base=2)	
		
		def control(func, num):
		    return func(num)
				
		ret01 = control(get_bin, "110")
		# control --> func(num)  ---> get_bin("110")
		print(ret01)
		
		ret02 = control(get_n, 10)
		print(ret02)
#### 匿名函数
* python 使用 lambda 来创建匿名函数。
* 
		结构
			lambda 参数1[参数2[参数3[...]]] : 表达式
			lambda [arg1 [,arg2,.....argn]]:expression
	* lambda 
		* 关键字   表示是一个匿名函数
	* 参数列表
		* 可以是一个参数，可以是多个参数，类型没有限制
	* ：
		* 上一句结束
	* 表达式
		* 返回值，或者匿名函数需要的操作
* 
		可以使用lambda创建小型的函数，实现简单的功能
		lambda指示一个表达式，不是代码块
		lambda可以访问表达式以外的变量
* 
		sum = lambda arg1, arg2: arg1 + arg2
 
		print ("相加后的值为 : ", sum( 10, 20 ))
		print ("相加后的值为 : ", sum( 20, 20 ))
		===>
		相加后的值为 :  30
		相加后的值为 :  40
#### 高阶函数
* 排序--sorted(iterable, key=None, reverse=False)
* 
		功能比sort()更强大
		可以对所有可迭代的对象进行排序操作
		返回的是一个新的 list
	* iterable -- 可迭代对象。
	* key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
	* reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
* 
		"""
		利用key进行倒序排序
		"""
		example_list = [5, 0, 6, 1, 2, 7, 3, 4]
		result_list = sorted(example_list, key=lambda x: x*-1)
		print(result_list)
		===>
		[7, 6, 5, 4, 3, 2, 1, 0]

		example_list = [5, 0, 6, 1, 2, 7, 3, 4]
		result_list = sorted(example_list, reverse=True)
		print(result_list)
		===>
		[7, 6, 5, 4, 3, 2, 1, 0]

		"""
		也可以通过 key 的值来进行数组/字典的排序
		""'
		array = [{"age":20,"name":"a"},{"age":25,"name":"b"},
		{"age":10,"name":"c"}]
		array = sorted(array,key=lambda x:x["age"])
		print(array)
		===>
		[{'age':10,'name':'c'}, {'age':20,'name':'a'}, {'age':25,'name':'b'}]
* map(function,iterable, ...)
	* 根据提供的函数对指定序列做映射，以参数序列中每一个元素调用function函数，返回值为包含每次function函数返回值的新列表。
	
	* Python3为返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
		* function---函数
		* interable---一个或多个序列
	* 
			list00 = [1,2,3,4,5]
			list01 = ["110","220","330","440"]
			ret01 = map(str,list00)
			ret02 = map(int,list01)
			print(ret01)
			print(list(ret01))
			print(ret02)
			print(list(ret02))
			===>
			<map object at 0x0000029B0958F9E8>
			['1', '2', '3', '4', '5']
			<map object at 0x0000029B0958FA58>
			[110, 220, 330, 440]
			
			**********************************************

			def square(x)：
	    		return x ** 2


			ret = map(square,[1,2,3,4,5])
			print(list(ret))
			===>
			[1,4,9,16,25]
	* 如果函数有多个参数, 但每个参数的序列元素数量不一样, 会根据最少元素的序列进行：
	* 
			listx = [1,2,3,4,5,6,7]       # 7 个元素
			listy = [2,3,4,5,6,7]         # 6 个元素 
			listz = [100,100,100,100]     # 4 个元素
			list_result = map(lambda x,y,z : x**2 + y + z,listx, listy, listz)
			print(list(list_result))
			===>
			[103, 107, 113, 121]
* 累积--reduce(function, iterable[, initializer])
	* 累积函数
	
	* 可以根据传入函数指定的规则对参数序列中元素进行累积，对元素进行运算，返回运算的结果
	
	* 先对序列中的第1，2个元素进行function函数运算，得到的结果再与第3个元素数据用function函数运算，依次进行，最后得到结果
		* function -- 函数，有两个参数
		* iterable -- 可迭代对象
		* initializer -- 可选，初始参数
	* Python3里需要导入
	* 
			from functools import reduce

			def add(x, y) :            # 两数相加
				return x + y
			
			reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
			===>
			15

			reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
			===>
			15

			#一行代码计算100以内所有数字的和
			print(reduce(lambda x,y:x + y,range(101)))			
* 过滤器--filter(function, iterable)
	* 过滤器
	* 过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
		* function -- 判断函数。
		* iterable -- 可迭代对象
	* 
			def is_odd(n):			
				return n % 2 == 1				#找出序列所有奇数

			list00 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

			tmplist = filter(is_odd,list00)
			print(tmplist)
			print(list(tmplist))
			===>
			<filter object at 0x00000262B5F3F4A8>
			[1, 3, 5, 7, 9]

			**********************************************
			
			list00 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
			
			get_ou = lambda x : x % 2 == 0		#找出序列所有偶数
			
			tmplist = filter(get_ou,list00)
			print(tmplist)
			print(list(tmplist))
			===>
			<filter object at 0x000002032CEDF3C8>
			[2, 4, 6, 8, 10]
* 偏函数--partial()
	* 偏--部分--以偏概全
	* 可以预设一部分参数，调用的时候传入参数的数目可以相应减少
	* 需要导入
	* 
			from functools import partial 
			
			def get_result(a,b):
    			return a / b

			ret = partial(get_result,10)
			print(ret)
			print(ret(2))
			===>
			functools.partial(<function get_result at 0x0000016258FC1E18>, 10)
			5.0

			ret = partial(get_result,b=2)
			print(ret)
			print(ret(10))
			===>
			functools.partial(<function get_result at 0x0000016258FC1E18>, b=2)
			5.0

			**********************************************
			
			def get_int(str,base):
				return int(str,base)

			print(get_int("1100",10))
			print(get_int("1100",2))
			===>
			1100
			12
			
			ret01 = partial(get_int,base=2)
			print(ret01("1100"))
			===>
			12

			ret01 = partial(get_int,"1100")
			print(ret01(2))
			===>
			12