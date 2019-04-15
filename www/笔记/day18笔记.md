## 18.01_Python语言基础(协程概述)(掌握)
* 协程
	* 又称微线程，纤程，是一种用户态的轻量级线程

* 发展历程：
	* 1、最初的生成器变形yield/send
    * 2、引入@asyncio.coroutine和yield from
    * 3、在最近的python3.5版本中引入了async/await关键字

* 理解协程：
    * 1、普通理解：
    	* 线程是系统级别的，他们是由操作系统调度。协程是程序级别的，由程序员根据需求自己调度。我们把一个线程中的一个个函数称为子程序，那么子程序在执行的过程中可以中断去执行别的子程序。别的子程序也可以中断回来继续执行之前的子程序，这就是协程。也就是说同一线程下的一段代码1执行执行着就可以中断，然后去执行另一段代码2，当再次回来执行代码块1的时候，接着从之前中断的地方开始执行
    * 2、专业理解：
    	* 协程拥有自己的寄存器上下文和栈，协程在调度切换时，将寄存器上下文和栈保存到其他的地方，在切回来时，恢复先前保存的寄存器上下文和栈。因此，协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态。


* 子程序：
	* 在所有的语言中都是层级调用，比如A中调用B，B在执行过程中调用C，C执行完返回，B执行完返回，最后是A执行完毕。是通过栈实现的，一个线程就是执行一个子程序，子程序的调用总是有一个入口，一次返回，调用的顺序是明确的


* 优点：
    * 1、无需线程上下文切换的开销，协程避免了无意义的调度，由此提高了性能，但是，程序员必须自己承担调度的责任，同时协程也失去了标准线程使用多CPU的能力
    * 2、无需原子操作锁定及同步的开销
    * 3、方便切换控制流，简化编程模型
    * 4、高并发+高扩展性+低成本，一个CPU支持上万个协程不是问题


* 缺点：
    * 1、无法利用多核资源，协程的本质是单个线程，它不能同时将单个CPU的多个核使用上，协程需要和进程配合使用才能运行在多CPU上。但是一般不需要，除非是CPU密集型的应用
    * 2、进行阻塞操作(耗时IO)会阻塞整个程序
####
	# def A():
	#     def B():
	#         def C():
	#             pass
	#         C()
	#     B()
	# A()
	
	
	def A():
	    print(1)
	    print(2)
	    print(3)
	def B():
	    print("a")
	    print("b")
	    print("c")

	协程可能实现其他的打印效果
	1
	2
	a
	b
	3
	c


## 18.02_Python语言基础(协程运行原理)(掌握)
#### 协程案例
	def func():
	    data = "#"
	    # yield不但可以返回一个值，并且它还可以接收调用者发送的参数
	    r = yield data
	    print("-------------1", r, data)
	    r = yield data
	    print("-------------2", r, data)
	    r = yield data
	    print("-------------3", r, data)
	    r = yield data
	
	
	g = func()
	print(g, type(g))
	print(next(g))
	print(next(g))
	# print(next(g))
	# print(next(g))
	# 启动g
	# print(g.send(None))
	# print(g.send("a"))
	# print(g.send("b"))
	# print(g.send("c"))


#### 案例02
	# 使用debug查看运行过程
	def run():
	    data = yield
	    print("1==", data)
	    data = yield
	    print("=2=", data)
	    data = yield
	    print("3==", data)
	    data = yield
	    print("=4=", data)
	    data = yield
	
	
	f = run()
	f.send(None)
	f.send("A")
	f.send("B")
	f.send("C")
	f.send("D")


## 18.03_Python语言基础(协程实现消费者和生产者)(掌握)
#### 乞丐版
	import time
	
	
	def consumer():
	    while True:
	        data = yield
	        if not data:
	            return
	        print("【consumer】消费数据 %s" % data)
	
	
	c = consumer()
	
	c.send(None)
	
	for i in range(5):
	    print("[produce] 生产数据%d" % i)
	    c.send(str(i))
	    time.sleep(1)


#### 精装版
	import time


	def produce(c):
	    c.send(None)
	    for i in range(5):
	        print("【produce】生成数据%d" % i)
	        # 发送数据给消费者
	        c.send(str(i))
	        time.sleep(1)
	    c.close()
	
	
	def consumer():
	    while True:
	        data = yield
	        if not data:
	            return
	        print("[consumer] 消费数据%s" % data)
	
	
	c = consumer()
	produce(c)


