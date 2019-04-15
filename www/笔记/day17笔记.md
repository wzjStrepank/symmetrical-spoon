## 17.01_Python语言基础(多线程概述)(掌握)
* 线程：	
	* 什么是线程？
	* 线程（英语：thread）是操作系统能够进行运算调度的最小单位。
	* 它被包含在进程之中，是进程中的实际运作单位。
	* 一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务
* 多线程
	* 什么是多线程？
	* 多线程（英语：multithreading），是指从软件或者硬件上实现多个线程并发执行的技术。
	* 具有多线程能力的计算机因有硬件支持而能够在同一时间执行多于一个线程，进而提升整体处理性能。
	* 具有这种能力的系统包括对称多处理机、多核心处理器以及芯片级多处理（Chip-level multithreading）或同时多线程（Simultaneous multithreading）处理器。
	* 在一个程序中，这些独立运行的程序片段叫作“线程”（Thread），利用它编程的概念就叫作“多线程处理（Multithreading）”。
	* 具有多线程能力的计算机因有硬件支持而能够在同一时间执行多于一个线程（台湾译作“执行绪”），进而提升整体处理性能。


## 16.02_Python语言基础(单线程运行)(掌握)
#### 单线程执行代码案例
	import time
	
	
	def run01():
	    for i in range(5, 0, -1):
	        print("流水线一还剩下%d秒完成工作。。。" % i)
	        time.sleep(1)
	
	
	def run02():
	    for i in range(5, 0, -1):
	        print("流水线二还剩下%d秒完成工作。。。" % i)
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 开始工作
	    run01()
	    run02()
	
	    print("END")


## 17.03_Python语言基础(多线程运行)(掌握)
#### 多线程执行代码案例
	import threading
	import time
	
	
	def run01():
	    for i in range(5, 0, -1):
	        print("线程%s还剩下%d秒完成工作。。。" % (threading.currentThread().getName(), i))
	        time.sleep(1)
	
	
	def run02():
	    for i in range(5, 0, -1):
	        print("线程%s还剩下%d秒完成工作。。。" % (threading.currentThread().getName(), i))
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    th1 = threading.Thread(target=run01)
	    th2 = threading.Thread(target=run01)
	
	    # 开启线程
	    th1.start()
	    th2.start()


## 17.04_Python语言基础(线程开启顺序)(掌握)
#### 多线程执行代码顺序
	import threading
	import time
	
	
	def run01():
	    for i in range(5, 0, -1):
	        print("线程一还剩下%d秒完成工作。。。" % i)
	        time.sleep(1)
	
	
	def run02():
	    for i in range(5, 0, -1):
	        print("线程二还剩下%d秒完成工作。。。" % i)
	        # '\033[41m%s 拿到A锁\033[0m'
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    th1 = threading.Thread(target=run01)
	    th2 = threading.Thread(target=run02)
	
	    # 开启线程
	    th1.start()
	    th2.start()
	
	    # 插入线程
	    th1.join()
	    th2.join()
	
	    print("END==》")


## 17.05_Python语言基础(线程设置name和获取name)(掌握)
#### 多线程设置和获取name和传入参数和彩色输出
	"""
	设置线程名字
	    Thread中有形参--name
	获取线程名字
	    threading.currentThread().getName()
	"""
	import threading
	import time
	
	
	def run01():
	    for i in range(5, 0, -1):
	        print("%s线程还剩下%d秒完成工作。。。" % (threading.currentThread().getName(), i))
	        time.sleep(1)
	
	
	def run02():
	    for i in range(5, 0, -1):
	        print("\33[40;37m%s线程还剩下%d秒完成工作。。。\33[0m" % (threading.currentThread().getName(), i))
	        # '\033[41m%s 拿到A锁\033[0m'
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    th1 = threading.Thread(target=run01, name="1号")
	    th2 = threading.Thread(target=run02, name="2号")
	
	    # 开启线程
	    th1.start()
	    th2.start()
	
	    # 插入线程
	    th1.join()
	    th2.join()
	
	    print("END==》%s" % threading.currentThread().getName())


## 17.06_Python语言基础(多线程修改全局变量)(掌握)
#### 多线程修改全局变量案例
	import time
	import threading
	
	num = 10
	
	
	def run01():
	    global num
	    for i in range(5):
	        print("hahaha", num)
	        num += 1
	        time.sleep(1)
	
	
	def run02():
	    global num
	    for i in range(5):
	        print("呵呵呵", num)
	        num += 1
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    t1 = threading.Thread(target=run01)
	    t2 = threading.Thread(target=run02)
	
	    # 开启线程
	    t1.start()
	    t2.start()
	
	    # 插入线程
	    t1.join()
	    t2.join()
	
	    print("END,num=", num)
* 线程不安全


## 17.07_Python语言基础(多线程修改全局变量--lock)(掌握)
#### 多线程修改全局变量--lock--案例
	import time
	import threading
	
	num = 10
	lock = threading.Lock()
	
	
	def run01():
	    global num
	    for i in range(5):
	        lock.acquire()
	        print("hahaha", num)
	        num += 1
	        lock.release()
	        time.sleep(1)
	
	
	def run02():
	    global num
	    for i in range(5):
	        lock.acquire()
	        print("呵呵呵", num)
	        num += 1
	        lock.release()
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    t1 = threading.Thread(target=run01)
	    t2 = threading.Thread(target=run02)
	
	    # 开启线程
	    t1.start()
	    t2.start()
	
	    # 插入线程
	    t1.join()
	    t2.join()
	
	    print("END,num=", num)

* 上锁保证数据安全--画图




## 17.08_Python语言基础(多线程--死锁)(掌握)
#### 多线程死锁案例
	import time
	import threading
	import random
	
	num = 10
	lock01 = threading.Lock()
	lock02 = threading.Lock()
	
	
	def run01():
	    global num
	    for i in range(5):
	        lock01.acquire()
	        print('\033[41m%s 拿到A锁\033[0m' % threading.currentThread())
	        lock02.acquire()
	        print('\033[41m%s 拿到B锁\033[0m' % threading.currentThread())
	        print("hahaha", num)
	
	        lock02.release()
	        lock01.release()
	
	        num += 1
	        # time.sleep(1)
	
	
	def run02():
	    global num
	    for i in range(5):
	        lock02.acquire()
	        print('\033[41m%s 拿到A锁\033[0m' % threading.currentThread())
	        lock01.acquire()
	        print('\033[41m%s 拿到B锁\033[0m' % threading.currentThread())
	
	        print("呵呵呵", num)
	
	        lock01.release()
	        lock02.release()
	        num += 1
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    t1 = threading.Thread(target=run01)
	    t2 = threading.Thread(target=run02)
	
	    # 开启线程
	    t1.start()
	    t2.start()
	
	    # 插入线程
	    t1.join()
	    t2.join()
	
	    print("END,num=", num)


## 17.09_Python语言基础(自定义线程)(掌握)
#### 自定义线程形成案例（下面的案例包含自定义线程和死锁）
	from threading import Thread, Lock
	import time
	
	lock01 = Lock()
	lock02 = Lock()
	
	
	class MyThread(Thread):
	    def run(self):
	        self.func01()
	        self.func02()
	
	    def func01(self):
	        lock01.acquire()
	        print("得到锁A:%s" % self.name)
	        lock02.acquire()
	        print("得到锁B:%s" % self.name)
	        lock02.release()
	        lock01.release()
	
	    def func02(self):
	        lock02.acquire()
	        print("得到锁A:%s" % self.name)
	
	        time.sleep(2)
	
	        lock01.acquire()
	        print("得到锁B:%s" % self.name)
	        lock01.release()
	        lock02.release()
	
	
	if __name__ == "__main__":
	    for i in range(5):
	        th = MyThread()
	        th.start()

## 17.10_Python语言基础(ThreadLocal)(掌握)
#### ThreadLocal（线程内部的属性）
	import time
	import threading
	
	num = 10
	local = threading.local()
	local.num = 50
	
	
	def run01():
	    for i in range(3):
	        local.num = 20
	        print("hahaha", local.num)
	        time.sleep(1)
	
	
	def run02():
	    for i in range(3):
	        local.num = 30
	        print("hehehehe%s" % local.num)
	        time.sleep(1)
	
	
	if __name__ == "__main__":
	    # 创建线程
	    t1 = threading.Thread(target=run01)
	    t2 = threading.Thread(target=run02)
	    
	    # 开启线程
	    t1.start()
	    t2.start()
	    
	    # 加入线程
	    t1.join()
	    t2.join()
	
	    print("END,num=", local.num)
	    print("END,num=", num)


## 17.11_Python语言基础(定时线程)(掌握)
#### 定时线程案例
	import threading
	
	
	def run():
	    print("lalala")
	
	
	if __name__ == "__main__":
	    # 创建定时线程
	    th = threading.Timer(3, run)
	
	    # 开启并加入定时线程
	    print("线程将于3秒后开启")
	    th.start()
	    th.join()
	
	    print("线程执行结束")


## 17.12_Python语言基础(线程通信)(掌握)
#### 线程通讯案例
	import threading
	import time
	
	
	def func():
	    # 获取线程时间对象
	    event = threading.Event()
	
	    def run():
	        for i in range(10):
	            # 线程等待状态
	            event.wait()
	            print("lalalla")
	            # 清除状态
	            event.clear()
	
	    # 函数内部创建开启线程
	    th = threading.Thread(target=run)
	    th.start()
	    return event
	
	
	# 调用函数返回event
	event = func()
	for i in range(10):
	    # 每个一秒解除等待状态
	    event.set()
	    time.sleep(1)


