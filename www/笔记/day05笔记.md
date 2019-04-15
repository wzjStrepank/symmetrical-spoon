## 函数
#### 函数概述
* 完成一定功能的代码块
* 提高代码的复用性，提高开发效率
* 方便管理
#### 格式
	def 函数名字(参数列表)：
		代码块
		return 变量/表达式
* def
	* 关键字----函数的关键字
* 函数名
	* 表示这个代码块的名字，调用这些代码时使用的名字
	* 合法的标识符
* (参数列表) 
	* 参数列表中可以添加任意个数的参数，理论上无数量上限，一般不会太多
	* 参数有很多种
		* args
		* *args
		* **kwargs
		* 参数列表中的参数可以在函数的代码块中使用
		* 调用函数时需要传入指定数目、类型的参数才能合法调用这个函数
* ：
	* 上一句代码结束，准备开始下一句
* 代码块
	* 此函数具体完成的操作
* 返回值(return)
	* 返回，通常表示函数运行到此结束
	* 返回的可以是变量、常量、表达式、函数、对象等
	* 返回内容可以为空，此时默认返回None
#### 函数分类
* 根据参数列表的返回值可以把函数分为四种

* 第一种：
	* 无参数，无返回值
	* 
			def notice():
				print("请站稳扶好，注意脚下安全")
			

			notice()
			===>
			请站稳扶好，注意脚下安全
	* 无参数，有返回值
	* 
			def get_info():
				return "您的电脑CPU型号是i9 9600K，硬盘大小是：2T...."
			

			info = get_info()
			print(info)
			===>
			您的电脑CPU型号是i9 9600K，硬盘大小是：2T....
	* 有参数，无返回值
	* 
			result = print("lalala")
			print(resunt)
			===>
			None
	* 有参数，有返回值
	* 
			def get_result(a,b):
				return a ** b
			

			result = get_result(3,2)
			print(result)
			===>
			9
#### 函数参数
* 调用函数时，传入的参数数目要和定义时的数目一致
* 传入的参数，顺序要和定义的时候一致
* 
		def show(name, addr):
	   		print("这个人的名字是：%s,他家住在：%s。" % (name, addr))


		show("秦奋", "黄土高坡")
		show("黄土高坡", "秦奋")
		===>
		这个人的名字是：秦奋,他家住在：黄土高坡。
		这个人的名字是：黄土高坡,他家住在：秦奋。
* 不定长参数之元组----*args
	* 长度不固定的参数----函数能处理比定义时更多参数
	
	* 在函数列表中使用参数*args，可以接受比定义的更多的参数
	* *args本质上是一个元组
	* 
			def show01(*args):
	    		print(args)
				print(type(args))


			show01("a", "b", "c", "d", "e")
			===>
			('a', 'b', 'c', 'd', 'e')
			<class 'tuple'>

			show01()
			===>
			()
			<class 'tuple'>	
	* 不定长参数一定要放在固定参数后面否则后面的固定参数无法接受数据
	* 
			def show03(name, sex, *args):
	    		print("这个人的名字是%s，性别是%s，还有一些其他特征%s" % (name, sex, args))


			show03("张三", "男", "个子很高", "长得很帅")
			===>
			这个人的名字是张三，性别是男，还有一些其他特征('个子很高', '长得很帅')
* 关键字参数
	* 在调用函数时可以指定某些参数的值，这样可以不按照顺序传参
* 
		def get_div(a,b):
			result = a / b
			return result


		ret = get_div(3,5)
		print(ret)
		===>
		0.6

		ret = get_div(b=5,a=3)
		print(ret)
		===>
		0.6
* 默认参数： 有默认值的参数
	* 有默认值得形参在调用时可以省略一些参数
	
	* 定义的时候，有默认值得参数必须写在无默认值参数的后面
	
	* 调用的时候，可以传入足量的参数，也可以省略某些带有默认值的
	* 参数传入的时候会按照形参定义的顺序赋值
	* 
			def get_square(x,y=2):
				return x ** y
	
			ret = get_square(5)
			print(ret)
			===>
			25
	
			ret = get_square(5,3)
			print(ret)
			===>
			125
	
			ret = get_square(5,y=3)
			print(ret)
			===>
			125
	
			ret = get_square(x=3,y=3)
			print(ret)
			===>
			27
	
			ret = get_square(x=5)
			print(ret)
			===>
			25
* 不定长参数之字典----**kwargs
* 
		def show00(name,age,*args,**kwargs):
			print(name,age,args,kwargs)


		show00("张三",18)
		show00("张三",18,"高","富","帅")
		show00("张三",18,"高","富","帅",sex="男",hobby="乐器")
		===>
		张三 18 () {}
		张三 18 ('高', '富', '帅') {}
		张三 18 ('高', '富', '帅') {'sex': '男', 'hobby': '乐器'}

		show00("李斯",2200,"身高七尺","富可敌国",)

#### 值传递和引用传递（复制07代码）
* 不可变类型参数
	* 传递的是值
	* 在函数运行结束后，不管函数中怎么修改这个值，外部定义的变量值不变
	* 
			num = 20
	
	
			def change_num(num):
			    num = num + 30
			    print(id(num))
			    return num
	
	
			print(change_num(num))
			print(id(num))
			print(num)
			===>
			1831170608
			50
			1831169648
			20
* 可变类型参数
	* 传递的是引用
	* 如果在函数中改变了这个参数的值，那这个参数就真的发生了改变
	* 
			list00 = [1, 2, 3, 4]
	
	
			def change_list(list00):
			    list00.append(5)
			    print(id(list00))
			    return list00
			
			
			change_list(list00)
			print(id(list00))
			print(list00)
			===>
			2406384871176
			2406384871176
			[1, 2, 3, 4, 5]
