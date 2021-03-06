from multiprocessing import Pool, pool
import os
from time import sleep


def func1(name):
    print(f"当前进程的ID：{os.getpid()}, {name}")
    sleep(2)
    return name


def func2(args):
    print(args)


if __name__ == "__main__":
    # 创建5个进程的进程池
    pool = Pool(5)

    pool.apply_async(func=func1, args=("sxt1", ), callback=func2)
    pool.apply_async(func=func1, args=("sxt2", ), callback=func2)
    pool.apply_async(func=func1, args=("sxt3", ), callback=func2)
    pool.apply_async(func=func1, args=("sxt4", ))
    pool.apply_async(func=func1, args=("sxt5", ))
    pool.apply_async(func=func1, args=("sxt6", ))
    pool.apply_async(func=func1, args=("sxt7", ))
    pool.apply_async(func=func1, args=("sxt8", ))

    # 关闭进程池
    pool.close()

    # 回收进程池
    pool.join()

x = "The are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print(x)
print(y)
