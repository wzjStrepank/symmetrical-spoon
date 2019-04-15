import time, random,os
from multiprocessing import Process

class DemoProcess(Process):
    def __init__(self, name):
        super(DemoProcess, self).__init__()
        self.name = name

    def run(self):
        print("子进程（%s--%s）启动，(父进程：%s)" % (self.name, os.getpid(), os.getppid()))
        for i in range(5):
            print("hahahahha--%d" %i)
            time.sleep(2)
        print("子进程（%s--%s）结束，(父进程：%s)" % (self.name, os.getpid(), os.getppid()))

    # 创建进程对象

if __name__ == "__main__":
    print("主进程开启")
    p1 = DemoProcess("dushine2008")
    p1.start()

    for i in range(5):
        print("lalalla--%d"%i)
        time.sleep(1)