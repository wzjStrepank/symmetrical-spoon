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
    cons.join()
    # cons.terminate()
    print("主进程结束")
