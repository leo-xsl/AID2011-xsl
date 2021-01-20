from multiprocessing import Process
from time import sleep
import os
import sys


def func01():
    print("我是第一个")
    print(os.getppid(), "---", os.getpid())


def func02():
    sleep(2)
    print("我是第二个")
    print(os.getppid(), "---", os.getpid())


def func03():
    sleep(3)
    # sys.exit("退出了")
    print("我是第三个")
    print(os.getppid(), "---", os.getpid())


list01 =[]
for i in [func01, func02, func03]:
    p = Process(target=i)
    list01.append(p)
    p.start()


for item in list01:
    item.join()