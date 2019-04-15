## 16.01_Python语言基础(多线进程概述)(掌握)
* 多任务
	* 操作系统可以同时运行多个任务，现代的操作系统比如Windows、Mac OS X、Linux、Unix等都是支持多任务的系统
* 单核CPU实现多任务的原理
	* 画图 
* 多核CPU实现多任务的原理
	* 画图
* 为什么要实现多任务
	* 提高工作效率
* 实现多任务的方式
	* 多进程模式
		* 启动多个进程，每个进程虽然只有一个线程，但是多个进程可以一起执行多个任务
	* 多线程模式
		* 启动一个进程，在一个进程的内部启动多个线程，这样多个线程也可以一起执行多个任务
	* 多进程+多线程
		* 启动多个进程，每个进程再启动多个线程
	* 协程
	* 多进程+协程


## 16.02_Python语言基础(多进程概述)(掌握)
* 进程
	* 进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。
	* 在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代面向线程设计的计算机结构中，进程是线程的容器。
	* 程序是指令、数据及其组织形式的描述，进程是程序的实体
	* 对于操作系统来说，一个任务就是一个进程。
	* 比方说打开浏览器就是启动一个浏览器的进程，在打开一个记事本就启动一个记事本进程，如果打开两个记事本就启动两个记事本进程。


## 16.03_Python语言基础(单进程执行任务)(掌握)
#### 单进程执行任务案例
	from time import sleep
	
	def run():
	    while True:
	        print("lalala")
	        sleep(1)
	
	if __name__ == "__main__":
	    while True:
	        print("heiheiheihei")
	        sleep(1.2)
	    # 不会执行到run方法，只有上面的while循环结束才行
	    run()
#### 两个耗时操作同时执行案例---单进程
	import time
	
	
	def run01():
	    for i in range(5):
	        print("lala", i)
	        time.sleep(1)
	
	
	def run02():
	    for i in range(5):
	        print("哈哈", i)
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    start_time = time.time()

	    run01()
	    run02()
	
	    end_time = time.time()
	    print("总共耗时%f", (end_time - start_time))


## 16.04_Python语言基础(多进程执行任务)(掌握)
#### 多进程执行任务案例
	from multiprocessing import Process
	from time import sleep
	
	'''
		multiprocessing模块
		1、跨平台的多进程模块
		2、提供了一个Process类代表一个进程对象
	'''
	
	def run(name, description):
	    while True:
	        print("%s is a %s man!"%(name, description))
	        sleep(1)
	
	if __name__ == "__main__":
	    #程序启动的进程称为主进程(父进程)
	
	    #创建进程(子进程)
	    p = Process(target=run, args=("小明", "handsome"))
	    #启动子进程
	    p.start()
	
	    while True:
	        print("小黑 is a nice man")
	        sleep(1)
#### 两个耗时操作同时执行案例---多进程
	import time
	from multiprocessing import Process
	
	
	def run01():
	    for i in range(5):
	        print("lala", i)
	        time.sleep(1)
	
	
	def run02():
	    for i in range(5):
	        print("哈哈", i)
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    start_time = time.time()
	    """
	    p1 = Process(target=run01)
	    p2 = Process(target=run02)
	    p1.start()
	    p2.start()
	    p1.join()
	    p2.join()
	    """
	    run01()
	    run02()
	
	    end_time = time.time()
	    print("总共耗时%f", (end_time - start_time))




## 16.05_Python语言基础(主进程和子进程顺序)(掌握)
#### 进程运行顺序案例
	from multiprocessing import Process
	from time import sleep
	
	def run():
	    print("启动子进程")
	    sleep(3)
	    print("结束子进程")
	
	def run2():
	    print("启动子进程2")
	    sleep(3)
	    print("结束子进程2")
	
	if __name__ == "__main__":
	    print("启动主进程")
	
	    p = Process(target=run)
	    p.start()
	
	    p2 = Process(target=run2)
	    p2.start()
	
	    # 主进程的结束不能影响子进程，所以可以等待子进程结束在结束主进程
	    # 等待子进程结束，才能继续执行主进程
	    # 后期主进程主要做的是调度相关的工作，不具体负责业务逻辑
	    p.join()
	    p2.join()
	    print("结束主进程")




## 16.06_Python语言基础(多条进程修改全局变量)(掌握)
#### 多条进程修改全局变量案例
	import time
	from multiprocessing import Process
	
	num = 10
	
	
	def run01():
	    global num
	    print("进程一开启")
	    time.sleep(2)
	    print("进程一修改数据")
	    print("进程一输出修改之前的num=", num)
	    num = 100
	    print("进程一输出num=", num)
	    time.sleep(2)
	
	
	def run02():
	    global num
	    print("进程二开启")
	    time.sleep(2)
	    print("进程二修改数据")
	    print("进程二输出修改之前的num=", num)
	    num = 200
	    print("进程二输出修改之后的num=", num)
	    time.sleep(2)
	
	
	if __name__ == "__main__":
	    p1 = Process(target=run01)
	    p2 = Process(target=run02)
	    p1.start()
	    p2.start()
	
	    p1.join()
	    p2.join()
	    print("主进程中的num=", num)




## 16.07_Python语言基础(开启大量子进程)(掌握)
#### 开启大量子进程案例
	from multiprocessing import Process, Pool
	import random, os, time
	
	
	def run(name):
	    print("%d子进程启动--%d" % (name, os.getpid()))
	    time.sleep(random.random() * 5)
	    print("%d子进程结束--%d====" % (name, os.getpid()))
	
	
	if __name__ == "__main__":
	    print("启动主进程")
	    """
	    进程池
	    表示可以同时进行的进程的数量
	    pool默认值为CPU的核心数，如果有4个核心，至少需要5个进程才能看到等待的效果
	    """
	    pool = Pool()
	    for i in range(5):
	        # 创建进程放入进程池中统一管理
	        pool.apply_async(run, args=(i,))
	
	    # 放入进程完毕，关闭进程池
	    pool.close()
	    # 调用join方法，开启pool中的所有进程
	    pool.join()
	
	    print("主进程结束")


## 16.08_Python语言基础(封装进程对象)(掌握)
* 编写类继承Process，重写run方法，创建对象后可以达到和开启进程相同效果
#### 封装进程对象案例
	# 创建进程类
	class DemoProcess(Process):
	    def __init__(self, name):
	        super(DemoProcess, self).__init__()
	        self.name = name
	
	    def run(self):
	        print("子进程（%s--%s）启动，(父进程：%s)" % (self.name, os.getpid(), os.getppid()))
	        for i in range(5):
	            print("hahahahha--%d"%i)
	            time.sleep(1)
	        print("子进程（%s--%s）结束，(父进程：%s)" % (self.name, os.getpid(), os.getppid()))

	# 创建进程对象
	import time, random
	from Day16.demo.demoProcess import DemoProcess
	if __name__ == "__main__":
	    print("主进程开启")
	    p1 = DemoProcess("dushine2008")
	    p1.start()
	
	    for i in range(5):
	        print("lalalla--%d", i)
	        time.sleep(random.random() * 5)


## 16.09_Python语言基础(多进程遍历目录)(掌握)
* 多进程执行程序有的时候耗费的时间更长
#### 遍历目录==》常规方式
	path = r"D:\File\HZ1901\Day15"
	file_list = os.listdir(path)
	t1 = time.time()
	for file_name in file_list:
	    abs_path = os.path.join(path, file_name)
	    if os.path.isdir(abs_path):
	        files = os.listdir(abs_path)
	        for file in files:
	            print(os.path.join(abs_path, file))
	t2 = time.time()
	print(t2 - t1)

#### 遍历目录==》多进程方式
	def run(path):
	    files = os.listdir(path)
	    for file in files:
	        print(os.getpid(), "<===>", os.path.join(path, file))
	
	
	if __name__ == "__main__":
	    path = r"D:\File\HZ1901\Day15"
	    file_list = os.listdir(path)
	    t1 = time.time()
	
	    pool = multiprocessing.Pool()
	    for file_name in file_list:
	        abs_path = os.path.join(path, file_name)
	        pool.apply_async(run, args=(abs_path,))
	    pool.close()
	    pool.join()
	
	    t2 = time.time()
	    print(t2 - t1)




## 16.10_Python语言基础(进程间通讯)(掌握)
* 进程间通讯方式
	* 有名管道
	* 无名管道
	* 队列
	* 共享内存
	* 信号
	* 信号量
#### 进程间通讯案例---队列
	import time
	from multiprocessing import Process, Queue
	
	
	def consumer(q):
	    print("开启consumer进程。。。")
	    while True:
	        print("consumer等待数据。。。")
	        # 获取队列中的内容
	        value = q.get(True)
	        print("consumer获取到数据%s" % value)
	    print("consumer进程结束。。。")
	
	
	def product(q):
	    print("product进程开启。。。")
	    time.sleep(3)
	    # 把数据放入队列
	    for i in ["hello", "world", "HelloWorld", "HelloPython"]:
	        print("将%s放入队列" % i)
	        q.put(i)
	        time.sleep(2)
	    print("product进程结束。。。")
	
	
	if __name__ == "__main__":
	    # 创建队列
	    q = Queue()
	    cons = Process(target=consumer, args=(q,))
	    prod = Process(target=product, args=(q,))
	    # 开启进程
	    prod.start()
	    cons.start()
	    
	    # 进程执行结束前插队
	    prod.join()
	    # cons.join()
	    cons.terminate()
	    print("主进程结束")
