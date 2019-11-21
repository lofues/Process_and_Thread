import multiprocessing


def f(p):
    print('(%s) 进程正在写入数据'%multiprocessing.current_process().pid)
    p.send('python')


if __name__ == '__main__':
    # 创建进程间通信的管道
    p1,p2 = multiprocessing.Pipe()
    # 创建子进程
    child_p = multiprocessing.Process(target=f,args=(p1,))
    # 子进程启动
    child_p.start()
    # 父进程接受数据
    print('(%s) 进程正在读取数据'%multiprocessing.current_process().pid)
    print(p2.recv())
    child_p.join()