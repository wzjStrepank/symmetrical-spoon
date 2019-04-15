## 09.01_Python语言基础(文件概述)(熟练)
#### 文件概述：
* 常见的文件格式：   txt  avi  html  zip  doc

#### 文件的作用


* 文件作用：把数据存储起来





## 09.02_Python语言基础(文件打开关闭)(掌握)
#
	我们日常中操作文件的过程：
	打开一个文件 ，或者新建一个文件
	读写数据
	关闭文件


#### Python语言中文件的打开

#
	在python中，使用open()函数可以打开一个已经存在的文件，或者创建一个新的文件
	格式：
	   open(文件名，访问模式)
	
	f = open("test.txt","w")
#### 访问模式概述
#    	
	访问模式                  说明
	w	打开一个文件只用于写入，如果该文件已经存在则将其覆盖，如果不存在，创建新文件
	r   以只读的方式打开一个文件，文件的指针将会在文件的开头位置，默认模式，如果文件不存在会报错
	a   打开一个文件用于追加，如果该文件已经存在，文件的指针会放在文件的结尾，即新的内容将会写入已有内容之后，如果文件不存在，如果文件不存在，创建以一个新文件进行写入
	
	rb	以二进制的方式打开一个文件用于只读，文件的指针将会在文件的开头位置，默认模式，如果文件不存在会报错
	wb  以二进制的格式打开一个文件只用于写入，如果该文件已经存在则将其覆盖，如果不存在，创建新文件
	ab	以二进制方式打开一个文件用于追加，如果该文件已经存在，文件的指针会放在文件的结尾，即新的内容将会写入已有内容之后，如果文件不存在，如果文件不存在，创建以一个新文件进行写入
	
	r+	打开一个文件用于读写，文件的指针放在文件的开头位置
	w+	打开一个文件用于读写,如果该文件已经存在将其覆盖，如果文件不存在，创建一个新文件
	a+	打开一个文件用于读写，文件的指针放在文件的末尾位置，，即新的内容将会写入已有内容之后，如果文件不存在，如果文件不存在，创建以一个新文件进行写入
	
	rb+	以二进制的方式打开一个文件用于读写，文件的指针放在文件的开头位置
	wb+	以二进制的方式打开一个文件用于读写,如果该文件已经存在将其覆盖，如果文件不存在，创建一个新文件
	ab+	以二进制的方式打开一个文件用于读写，文件的指针放在文件的末尾位置，，即新的内容将会写入已有内容之后，如果文件不存在，如果文件不存在，创建以一个新文件进行写入



#### Python语言中文件的关闭

#
	使用函数：
	close()
	f = open("test.txt","w")
	f.close()
	
	"""
>注意:<br/>
	close（）作用---》节省内存
***







## 09.03_Python语言基础(文件的读写)(掌握)
#### 写数据（write）
#
	使用write()函数可以完成对文件写入内容
	格式:
	   f.write(str)

	f = open("test.txt","w")
	f.write("hello world !")
	f.close()

>注意:<br/>
    如果文件不存在则创建,如果存在,则先清空,在写入数据
***



#### 读取数据（read/readline/readlines）

#
	1.读取数据使用read()函数，可以从文件中读取数据,
	格式:
	read(num)
	num :  表示要从文件中读取的数据的长度(单位字节),
	如果num没有传入,那么表示读取文件的所有数据
	
	"""
	# f = open("test.txt")
	# content = f.read()
	# print(content)
	# content1 = f.read(5)
	# print(content1)
	# f.close()

>注意:
    如果使用了多次,那么后面读取的数据是从
    上一次读取完数据后的位置开始
***




#### 第二种方式：readlines
* 使用readlines可以按照行的方式把整个的文件中的内容进行一次性读取,
* 返回一个列表,其中每一行的数据作为一个元素
#
	f = open("test.txt", "r+")
	f.write("hello python \n hello python \n hello python \nhello python ")
	content = f.readlines()
	print(type(content))
	print(content)
	# 获取列表中所有的内容
	i = 1
	for temp in content:
	    print("%d:%s" % (i, temp))
	    i += 1
	f.close()
	运行输出结果：
	<class 'list'>
	['hello python \n', ' hello python \n', ' hello python \n', 'hello python ']
	1:hello python 
	2: hello python 
	3: hello python 
	4:hello python 






#### 再来一个例子


#
	readline:返回的数据是str
	f = open("test.txt","r")
	content = f.readline()
	print(type(content))
	content2 = f.readline()
	content3 = f.readline()
	
	print(content)
	print(content2) 
	print(content3)
	f.close()

	运行输出结果：
	******************************
	<class 'str'>
	hello python 
	
	 hello python 
	
	 hello python 




>思考:有一个很大的文件5G,怎样读取里面的数据(readline/read(num))
***
#### 读取CSV文件
#
	# Comma-Separated Values，CSV，有时也称为字符分隔值
	# 导入CSV模块  pdf   图片
	import csv
	def readCsv(path):
	    infoList = []
	    with open(path,"r") as f:
	        allFileInfo = csv.reader(f)
	        # print(type(allFileInfo))
	        for row in allFileInfo:
	            infoList.append(row)
	    return infoList
	path = r"E:\Files\杭州校区Python基础班\day13\资料\csv\000002.csv"
	info = readCsv(path)
	print(info)


#### 写入csv数据
#
	import csv
	def writeCsv(path,data):
	    with open(path,"w") as f:
	        writer = csv.writer(f)
	        for rowDate in data:
	              writer.writerow(rowDate)
	
	
	path = r"E:\Files\day09\资料\000002.csv"
	writeCsv(path,[["1","2","3"],["4","5","6"],["7","8","9"]])











## 09.04_Python语言基础(制作文件的备份)(掌握)

* 任务描述：
	* 输入文件名字，然后程序自动完成对该文件的备份操作：
#
	分析：
	   input()-->string
	   open()
	   判断用户输入的文件是否存在
	         存在 
	              1.打开文件
	              2.读取数据
	              3.关闭文件
	         不存在----》错误提示
	   
	   
	   完成备份：
	      1.拿到刚才读取到的数据
	      2.创建一个新文件，将刚才读取到的数据写到这个新文件中
	      3.关闭文件
   
# 
	oldFileName = input("请输入需要备份的文件:")
	#打开需要备份的文件
	oldFile = open(oldFileName,"r")
	#读取需要备份文件的内容
	#判断是否打开
	if oldFile:
	    #提取文件的后缀名
	    fileFlagNum = oldFileName.rfind(".")
	    if fileFlagNum > 0:
	        fileFlag = oldFileName[fileFlagNum]
	
	    #组织新文件的名字
	    newFilename = oldFileName[:fileFlagNum]+"[复件]"+fileFlag
	    #创建一个新的文件
	    newFile = open(newFilename,"w")
	    #将旧文件中的数据,一行一行的方式进行复制到新文件中
	    for lineContent in oldFile.readlines():
	        newFile.write(lineContent)
	
	    #关闭文件
	    oldFile.close()
	    newFile.close()











## 09.05_Python语言基础(文件的定位)(掌握)

* 定位：
	* 通俗的讲就是找到一个位置
#### 获取当前读写文件的位置
#
	"""
	获取当前读写文件的位置
	在读取文件的过程中,如果想知道当前的位置,
	可以使用函数tell()来获取,是光标开始的位置
	"""
	# 打开一个文件
	f = open("test.txt", "r")
	str = f.read(3)
	print(str)
	# 查找当前光标的位置
	position = f.tell()
	print(position)
	str = f.read(3)
	position = f.tell()
	print(position)
	f.close()


#### 定为到某一个位置
#
	如果在读写文件的过程中,需要从另外一个位置进行操作,可以使用seek()函数
	格式:
	seek(offset,from)
	offset:偏移量
	from:方向
	    0:表示文件的开头
	    1:表示当前位置
	    2:表示文件的末尾
	    
	案例L:
	把位置设置为:从文件的开头,偏移5个字节
	"""
	
	
	#打开一个文件
	f = open("test.txt","rb+")
	str = f.read(30)
	print(str)
	#查找光标当前的位置
	# position = f.tell()
	# print(position)
	#重新设置位置
	f.seek(-3,2)
	position = f.tell()
	print(position)
	f.close()


>注意:
   如果打开文件的模式"r",而不是"rb",则会报错
   在文本文件中,没有使用b模式选项打开文件,只允许从文件的开头计算相对位置
***










## 09.06_Python语言基础(文件的操作)(掌握)
#### 文件重命名
* 概述：
	* 需要对文件进行重命名操作，删除，python中有一个模块os模块----》文件的操作
	* os模块中有 一个函数rename()可以完成对文件名的重新命名
#
	格式和案例：
	rename(需要修改的文件名，，新的文件名)
	import os
	# os.rename("test.txt","毕业论文.txt")


#### 文件的删除
#
	概述：
	os模块中remove()可以完成对文件的删除操作   
	格式：
	remove(待删除的文件名)
	案例：
	os.remove("毕业论文.txt")


#### 创建一个文件夹

#
	概述：
	    使用os模块中mkdir()函数
	    
	 格式：
	 mkdir(str)
	
	
	案例：
	import os
	os.mkdir("张三")


#### 获取当前的目录

#
	概述：
	   使用os模块中listdir()函数   
	格式：
	  listdir()
	案例：
	import os
	print(os.listdir("./"))
	#结果为当前目录的文件



#### 删除文件夹

#
	概述：
	   使用os模块中的rmdir()函数
	 格式：
	     rmdir(str)  
	     str--->表示需要删除的文件夹名称
	案例：
	import os
	os.rmdir("张三")


#### 应用----批量修改文件名（重命名）










## 09.07_Python语言基础(StringIO和BytesIO)(熟练)

#### StringIO
* 很多时候，数据读写不一定是文件，也可能在内存中读写
* StringIO:在内存中读写str
#### StringIO案例：
#
	"""
	StringIO
	"""
	from io import StringIO
	f = StringIO()
	f1 = f.write("hello")#返回的是写入数据的字节数(每次写入的数据)
	print(type(f1))
	print(f1)#5
	f2 = f.write(" ")
	print(f2)#1
	f3 = f.write("world!")
	print(f3)#6
	print(f)
	print(f.getvalue())
	
	"""
	读取StringIO文件,可以用一个str初始化StringIO,
	"""
	f = StringIO("hello\nhi\ngoodbye!")
	while True:
	    s = f.readline()
	    if s == "":
	        break
	    print(s.strip())



#### BytesIO

	StringIO操作---》str
	如果操作二进制数据，需要使用BytesIO
	BytesIO实现在内存中读取byte数据









## 09.08_Python语言基础(异常概述)(掌握)
#### 异常的介绍

#
	print("------test-----1")
	open("123.txt","r")
	print("-----test------2")


>当python检测到一个错误时,解释器就无法继续执行,反而出现错误提示--->异常
***







## 09.09_Python语言基础(异常的处理)(掌握)

* 当出现异常的时候如何处理？
	* 捕获异常
#
	基本的格式：
	try....except....
	try:
	 需要捕获的异常代码
	except 异常处理的类型：
	 pass
	
	
	try:
	print("------test-----1")
	open("123.txt","r")
	except  FileNotFoundError:
	print("找不到该文件")
	print("-----test------2")
	print("-----test   3")



* 程序看不到任何错误,因为用来except,
* 捕获到FileNotFoundError异常,并添加了处理方法

>总结:
    把可能出现问题的代码,放在try里面,
    把异常处理的代码放在except中
***
* 思考:
	* 如果出现多个异常该如何处理?


#
	try:
	    print("------test-----1")
	    open("123.txt","r")
	except (IOError,NameError):
	    print("找不到该文件")
	print("-----test------2")
	print("-----test   3")
	"""
	报错,异常处理的类型不正确
	"""







## 09.10_Python语言基础(捕获多个异常)(掌握)
#
	try:
	    print("----test---1----")
	    print(AA.aa())
	    open("123.txt","r")
	    print("-----test-----2")
	except (NameError,FileNotFoundError):
	    print("----test   3")

* 当捕获多个异常时,可以把异常的捕获的名字,
* 放到except中,如果是多个使用元组的方式进行存储




#### 获取异常的信息

#
	try:
	    open("123.txt","r")
	except FileNotFoundError as ss:
	    # print("文件不存在....")
	    print(ss)
	
	"""
	关键字as as后面跟的是错误的描述信息errorMsg
	那么它的基本格式:
	    except (错误类型) as 错误的描述:
	        return 错误描述


#### 捕获所有的异常

#
	# exception
	try:
	    # open("133.txt","r")
	    # print(AA.aa())
	    print(abcd)
	    open("134.txt", "r")
	    print(AB.aa())
	    print(abcdaaa)
	except Exception as reslut:
	    print(reslut)










## 09.11_Python语言基础(else)(掌握)

* 概述：
	* 如果没有捕获到异常，那么执行else中的代码
#
	try:
	    num = 300
	    print(num)
	
	except NameError as errormsg:
	    print(errormsg)
	else:
	    print("没有捕获到异常,真高兴!")




## 09.12_Python语言基础(try...finally)(掌握)

* try...finally:
	 * 在程序中，如果一段代码必须要执行，无论异常是否产生都要去执行，那么此时需要使用finally
	* 如：文件的关闭，释放锁，把数据连接返回连接池
    
    
    
    




## 09.13_Python语言基础(异常的传递)(掌握)
* 异常的传递
	* 我们调用方法的时候，方法中可能出现错误，
    * 这个错误或传递到当前运行的主d代码中，需要做异常的处理
    * 可以再被调用的方法中处理，也可以在主代码中处理
#
	import os
	
	def demo13():
	    try:
	        os.remove("file")
	    except Exception as e:
	        print(e)
	
	
	def get_result(*args):
	    result = 0
	    for i in args:
	        result += i
	    return result
	
	
	while True:
	    select = int(input("请输入您的选择"))
	    if select == 1:
			# 可以再此处处理异常，也可以在被调用的函数中处理异常
	        # try:
	        #     demo13()
	        # except Exception as e:
	        #     print(e)
	        demo13()
	    elif select == 2:
	        print(get_result(1, 2, 3, 4, 5))
	    elif select == 3:
	        break
	    else:
	        print("输入有误")


## 09.14_Python语言基础(try嵌套)(掌握)
	"""
	IndexError
	ValueError
	ZeroDivisionError
	FileNotFoundError
	异常的嵌套
	    如果出现异常，那么这个异常子级的代码讲无法继续运行
	    和他平行的那一级可以正常运行
	"""
	
	print("代码开始运行")
	
	try:
	    print("异常处理的第一层")
	    try:
	        print(1 / (int(input("请输入一个整数:"))))
	        try:
	            print(input("请输入一个很长的字符串")[10])
	        except Exception as e:
	            print(e)
	        try:
	            print("我是很长字符串下面那句")
	        except Exception as e:
	            print(e)
	    except Exception as e:
	        print(e)
	except Exception as e:
	    print(e)
	
	print("代码运行结束")


#### 函数嵌套中调用

#
	class A(object):
	    pass
	
	def test1():
	    print("----test1----1")
	    print(A.hello())
	    print("------test1-----2")
	def test2():
	    print("----test2----1")
	    test1()
	    print("------test2-----2")
	
	def test3():
	    try:
	        print("----test3----1")
	        test1()
	        print("------test3-----2")
	    except Exception as reslut:
	        print(reslut)
	    finally:
	        print("nihao")

	test3()






## 09.15_Python语言基础(抛出自定义异常)(掌握)

* 如何定义一个自定义的异常
	* 需要使用raise语句用来引发异常
	* 异常和错误对象必须有一个名字，并且是error或者是exception的子类

* raise语句的基本的格式
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



