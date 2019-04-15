## 14.01python语言基础(python2和python3区别)(了解)

## 14.02python语言基础(入门算法--选择排序)(掌握)
#
	每次从待排序的数据中选取最小（最大）的一个元素，存放到序列的起始位置，直到全部排完
	[1,3,5,6,8,9,2,3,5,2,1]
#
	#选择排序
	#[1,2,3]
	def select_sort(list00):
    # 每次找到一个最大值，直到结束
    for i in range(len(list00) - 1, 0, -1):
        # 假设一个最大值
        max_one = 0
        # 用假设的最大值和全部元素比较，如果假设的最大值不成立，就把真正的最大值获取到
        for j in range(1, i + 1):
            if list00[j] > list00[max_one]:
                max_one = j
        # 把最大值放到最后
        list00[i], list00[max_one] = list00[max_one], list00[i]
    # 比较结束，返回排序后的列表
    return list00

	
	list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]
	print(select_sort(list01))







## 14.03python语言基础(入门算法--冒泡排序)(掌握)

* 第一次：相邻两个数相比，大的往右，最后一个元素就是最大值
* 第二次：相邻两个数相比，大的往右，最后一个元素就是最大值
* ....
#### 冒泡排序案例：
#
	#冒泡排序
	
	list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]


	def bubble_sort(list00):
	    # 每次比较的内容总数目减少一个
	    for i in range(len(list00) - 1, 0, -1):
	        # 比较相邻的两个元素，如果前面的元素比较大就换到后面
	        for j in range(i):
	            if list00[j] > list00[j + 1]:
	                list00[j], list00[j + 1] = list00[j + 1], list00[j]
	    return list00


	print(bubble_sort(list01))
	




## 14.04python语言基础(调试--打印)(掌握)
#### 打印
#
	#打印
	# def test(s):
	#     n = int(s)
	#     try:
	#         print(">>>n = %d"%n)
	#         return 10/n
	#         print(">>>n = %d" % n)
	#     except Exception:
	#         pass
	# def main():
	#     test("0")
	# main()

#### print的弊端，明文显示，将来要删除


## 14.05_python语言基础(调试--断言)(了解)
#### 断言
#
	"""
	断言  assert
	格式：assert 表达式

	def test(s):
	    n = int(s)
	    assert n != 0, 'n is zero'
	    return 10 / n
	
	
	def main():
	    test("1")
	
	
	main()

	assert  1 + 1 == 2
	
	assert isinstance("hello",str)
	assert isinstance("hello",int)

> 如果assert断言成功，assert语句本身同样抛出异常AssertionError，提示错误的内容就是后面的字符串
***




## 14.06python语言基础(调试--logging)(熟练)
* logging
	* 把print替换logging，和assert相比，logging不会出现异常，而且可以输出到文件
* 模块
	* 导入logging模块

####案例1：
	import logging
	logging.basicConfig(level=logging.INFO)
	s = "0"
	n = int(s)
	logging.info("n = %d"%n)
	print(10/n)
#### 案例2：
	import logging
	# 设置显示内容优先级
	logging.basicConfig(level=logging.INFO)
	n = 1
	
	for i in range(10):
	    n += i
	    logging.info(n)
	print(n)
	# 记录目标的
	"""
	DEBUG
	INFO
	NOTICE
	WARNING
	ERROR
	CRITICAL
	ALERT
	EMERGENCY
	"""

## 14.07python语言基础(调试--pdb)(了解)
#### pdb概述
#
	import pdb
	
	pdb
	pdb是python中自带的模块，
	作用：
	    为python程序提供一种交互的源代码调试功能
#### pdb案例：
#    
	import pdb
	def add01(a, b):
	    return a + b
	
	def add02(a, b):
	    pdb.set_trace()
	    c = add01(a, b)
	    print(c)
	
	add02(3, 6)

#### pdb命令提示符启动方式：
#
	启动pdb方式：
	   DOS--->当前目录---》python -m -pdb XXX.py（已经安装了python）
	   直接在PyCharm中导入运行
#### pdb常用命令
#
	命令           用途
	break 或则 b	设置断点
	continue/c	继续执行程序，或者跳到下一个断点
	next/n		执行下一行
	step/s		进入函数
	list/l      查看当前的代码段
	return/r    执行代码直到从当前函数的返回
	exit/q		终止，退出
	p/!			打印变量的值    p a
	help/h		帮助





## 14.08_python语言基础(调试--debug)(掌握)



## 14.09_python语言基础(单元测试--对函数进行测试)(熟练)
* 概述：
	* 单元测试：
       * 用来对一个函数，一个类或者一个模块来进行一个正确性的校验工作
       
* 结果：
   * 1.单元测试通过：说明测试的函数功能正常
   * 2.单元测试不通过：函数有BUG，测试条件输入有误


* 如果要使用单元测试---》python内置的模块unittest
#### 单元测试案例
	from Day17.Demos.demo01 import add_num, sub_num
	import unittest
	
	class Test(unittest.TestCase):
	    def setUp(self):
	        print("开始测试时候调用")
	
	    def tearDown(self):
	        print("测试结束时候调用")
	
	    def test_add(self):
	        self.assertEqual(add_num(1, 2), 4, "加法不行")
	
	    def test_sub(self):
	        self.assertEqual(sub_num(5, 3), 2, "减法不行")
	
	if __name__ == '__main__':
	    unittest





## 14.10_python语言基础(单元测试--对类进行测试)(熟练)
#### 1.创建Person模块
#	
	class Person(object):
	    def __init__(self,name,age):
	        self.name = name
	        self.age = age
	
	    def getAge(self):
	        return self.age

#### 2.进行自测：
	from Person import Person
	per = Person("xiaoming",29)
	print(per.getAge())

#### 3.单元测试
	import unittest
	
	from Day17.Demos.Person import Person
	
	
	class Test(unittest.TestCase):
	    def test_init(self):
	        xiao = Person("小", 30)
	        self.assertEqual(xiao.name, "小", "属性赋值错误")
	
	    def test_age(self):
	        xiao = Person("大", 28)
	        self.assertEqual(xiao.getAge(), 29, "年龄设置错误")
	
	
	if __name__ == '__main__':
	    unittest





## 14.11_python语言基础(单元测试--文档测试)(熟练)
* 如果要进行文档测试需要导入doctest模块
* doctest模块可以提取注释中的代码执行
#### 文档测试案例：
#
	import doctest
	
	def add_num(a, b, c):
	    """
	    :param a:
	    :param b:
	    :param c:
	    :return: sum
	
		注意空格
	    >>> print(add_num(1,2,3))
	    5
	    6
	    """
	    sum = a + b + c
	    return sum
	
	#进行文档测试
	doctest.testmod()


## 14.12_Python语言基础(TCP/IP概述)(了解)
* 对互联网大家都很熟悉，实际上计算机网络的出现比互联网要早很多。



#### 通讯协议
	计算机为了联网，就必须规定通信协议，都是由各厂商自己规定早期的计算机网络一套协议
	IBM、Apple和Microsoft都有各自的网络协议，互不兼容，这就好比一群人有的说英语，
	有的说中文，有的说德语，说同一种语言的人可以交流，不同的语言之间就不行了。
	
	为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，
	为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。
	Internet是由inter和net两个单词组合起来的，原意就是连接“网络”的网络，
	有了Internet，任何私有网络，只要支持这个协议，就可以联入互联网。



#### TCP\IP协议
	互联网协议包含了上百种协议标准，最重要的两个协议是TCP和IP协议，
	所以，大家经常把互联网的协议简称TCP/IP协议。



#### 通讯原理
	通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址。
	互联网上每个计算机的唯一标识就是IP地址，类似123.123.123.123。
	如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，
	所以，IP地址对应的实际上是计算机的网络接口，通常是网卡。



#### IP协议
	IP协议负责把数据从一台计算机通过网络发送到另一台计算机。
	数据被分割成一小块一小块，然后通过IP包发送出去。
	由于互联网链路复杂，两台计算机之间经常有多条线路，
	因此，路由器就负责决定如何把一个IP包转发出去。
	IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
	



#### TCP协议
	TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
	TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

	许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。




#### 端口
	一个IP包除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
	端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
	一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。
	每个网络程序都向操作系统申请唯一的端口号，
	这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
	一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。



## 14.13_Python语言基础(网络编程)(了解)
Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，
使主机间或者一台计算机上的进程间可以通讯。
Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。


Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
socket.socket([family[, type[, proto]]])
family: 套接字家族可以使AF_UNIX或者AF_INET
type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
protocol: 一般不填默认为0.



#### socket编程有UDP和TCP两种传输协议

## 14.14_Python语言基础(UDP编程)(熟练)
UDP则是面向无连接的协议。
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。
但是，能不能到达就不知道了。
虽然用UDP传输数据不可靠，但它的优点是速度快(和TCP比)，对于不要求可靠到达的数据，就可以使用UDP协议。
我们来看看如何通过UDP协议传输数据。使用UDP的通信双方分为客户端和服务器。
服务器首先需要绑定端口：

UDP编程步骤要简单许多，分别如下：
#
	 	 
#### UDP编程的服务器端一般步骤是： 
		"""
	　　1、创建一个socket，用函数socket()； 
	　　2、设置socket属性，用函数setsockopt();* 可选 
	　　3、绑定IP地址、端口等信息到socket上，用函数bind(); 
	　　4、循环接收数据，用函数recvfrom(); 
	　　5、关闭网络连接；
		"""
#### UDP客户端的client写法
import socket
* 创建socket对象
	* server_udp = socket.socket(type=socket.SOCK_DGRAM)
* 绑定地址和端口号
	* ip_port = ("172.16.5.236", 10086)
	* server_udp.bind(ip_port)
* 接收数据
  	* data, addr = server_udp.recvfrom(1024)
	* print(str(data, encoding="utf-8"))
* 断开连接
	* server_udp.close()

	
#### UDP编程的客户端一般步骤是： 
		"""
	　　1、创建一个socket，用函数socket()； 
	　　2、设置socket属性，用函数setsockopt();* 可选 
	　　3、绑定IP地址、端口等信息到socket上，用函数bind();* 可选 
	　　4、设置对方的IP地址和端口等属性; 
	　　5、发送数据，用函数sendto(); 
	　　6、关闭网络连接；
		"""

#### UDP客户端的client写法
import socket

* 创建socket,设置socket属性
	* client_udp = socket.socket(type=socket.SOCK_DGRAM)
* 设置目标IP地址和端口等属性; 
	* ip_port = ("172.16.5.236", 10086)
* 发送数据，用函数sendto(); 
	* msg = input("请输入要发送的信息：")
	* client_udp.sendto(bytes(msg, encoding="utf-8"), ip_port)
* 断开连接
	* client_udp.close()



## 14.15_Python语言基础(TCP编程)(熟练)
#### TCP服务端server的写法：
	* 创建 socket 套接字：
	* bind 绑定 
	* listen 监听
	* accept 接受请求连接
	* 接收数据
	* 断开连接
	

* 创建 socket 套接字：
	* server_tcp = socket.socket() 
* bind 绑定     
	* ip_port = ("172.16.5.236", 10086)
	* server_tcp.bind(ip_port)
* listen 监听      
	* server_tcp.listen(5)
* accept 接受请求连接
	* conn, addr = server_tcp.accept()
* 接收数据　　
	* data = conn.recv(1024)
	* print(str(data, encoding="utf-8"))
* 断开连接　　
	* conn.close()
	

#### TCP客户端的client写法
	* 创建socket对象
	* 确定IP
	* 建立客户端连接
	* 发送消息
	* 断开连接


* 创建socket对象
	* client_tcp = socket.socket()
* 确定IP
	* ip_port = ("172.16.5.236", 10086)
* 建立客户端连接
	* client_tcp.connect(ip_port)
* 发送消息
	* msg = input("请输入消息：")
	* client_tcp.sendall(bytes(msg, encoding="utf-8"))
* 断开连接
	* client_tcp.close()


## 14.16_Python语言基础(TCP编程加强版)(熟练)
#### 客户端加强版
	import socket
	
	# 创建socket对象
	client_tcp = socket.socket()
	ip_port = ("172.16.5.236", 10086)
	# 建立客户端连接
	client_tcp.connect(ip_port)
	
	while True:
	    # 发送消息
	    msg = input("请输入消息：")
	    if len(msg) == 0:
	        continue
	    elif msg == "exit":
	        break
	    client_tcp.sendall(bytes(msg, encoding="utf-8"))
	
	    # 接收消息
	    data = client_tcp.recv(1024)
	    print(str(data, encoding="utf-8"))
	
	# 断开连接
	client_tcp.close()


#### 服务端加强版
	import socket
	
	# 创建socket对象
	server_tcp = socket.socket()
	# 主机地址和端口号
	ip_port = ("172.16.5.236", 10086)
	# 绑定主机地址和端口号
	server_tcp.bind(ip_port)
	# 监听
	server_tcp.listen(5)
	# 建立客户端连接
	conn, addr = server_tcp.accept()
	
	while True:
	    # 接收消息
	    data = conn.recv(1024)
	    if not data:
	        break
	    else:
	        print(str(data, encoding="utf-8"))
	    # 回复消息
	    msg = input("请回复：").strip()
	    if len(data) == 0:
	        continue
	    conn.sendall(bytes(msg, encoding="utf-8"))
	
	# 断开连接
	conn.close()


## 14.17_Python语言基础(TCP和UDP比较)(熟练)
* TCP与UDP的区别
#### 基于连接与无连接 
	对系统资源的要求（TCP较多，UDP少） 
	UDP程序结构较简单 
	流模式与数据报模式 
	TCP保证数据正确性，UDP可能丢包 
	TCP保证数据顺序，UDP不保证 
	部分满足以下几点要求时，应该采用UDP 面向数据报方式 网络数据大多为短消息 
	拥有大量Client 
	对数据安全性无特殊要求 
	网络负担非常重，但对响应速度要求高 
	具体编程时的区别 socket()的参数不同 
	UDP Server不需要调用listen和accept 
	UDP收发数据用sendto/recvfrom函数 
	TCP：地址信息在connect/accept时确定 
	UDP：在sendto/recvfrom函数中每次均 需指定地址信息 
	UDP：shutdown函数无效

* 编程区别

#### UDP和TCP编程步骤也有些不同，如下： 
####TCP编程的服务器端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt(); * 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind(); 
	4、开启监听，用函数listen()； 
	5、接收客户端上来的连接，用函数accept()； 
	6、收发数据，用函数send()和recv()，或者read()和write(); 
	7、关闭网络连接； 
	8、关闭监听；

#### TCP编程的客户端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt();* 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind();* 可选 
	4、设置要连接的对方的IP地址和端口等属性； 
	5、连接服务器，用函数connect()； 
	6、收发数据，用函数send()和recv()，或者read()和write(); 
	7、关闭网络连接；

* 与之对应的UDP编程步骤要简单许多，分别如下： 
#### UDP编程的服务器端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt();* 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind(); 
	4、循环接收数据，用函数recvfrom(); 
	5、关闭网络连接；

#### UDP编程的客户端一般步骤是： 
	1、创建一个socket，用函数socket()； 
	2、设置socket属性，用函数setsockopt();* 可选 
	3、绑定IP地址、端口等信息到socket上，用函数bind();* 可选 
	4、设置对方的IP地址和端口等属性; 
	5、发送数据，用函数sendto(); 
	6、关闭网络连接；

