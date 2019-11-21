import multiprocessing
# 使用 Pipe 实现进程通信，程序会调用 multiprocessing.Pipe() 函数来创建一个管道，该函数会返回两个 PipeConnection 对象，
# 代表管道的两个连接端（一个管道有两个连接端，分别用于连接通信的两个进程）。
#
# PipeConnection 对象包含如下常用方法：
# send(obj)：发送一个 obj 给管道的另一端，另一端使用 recv() 方法接收。需要说明的是，该 obj 必须是可 picklable 的（Python 的序列化机制），
# 如果该对象序列化之后超过 32MB，则很可能会引发 ValueError 异常。

# recv()：接收另一端通过 send() 方法发送过来的数据。
# fileno()：关于连接所使用的文件描述器。

# close()：关闭连接。
# poll([timeout])：返回连接中是否还有数据可以读取。

# send_bytes(buffer[, offset[, size]])：发送字节数据。如果没有指定 offset、size 参数，则默认发送 buffer 字节串的全部数据；
# 如果指定了 offset 和 size 参数，则只发送 buffer 字节串中从 offset 开始、长度为 size 的字节数据。通过该方法发送的数据，应该使用 recv_bytes()
# 或 recv_bytes_into 方法接收。

# recv_bytes([maxlength])：接收通过 send_bytes() 方法发迭的数据，maxlength 指定最多接收的字节数。该方法返回接收到的字节数据。
# recv_bytes_into(buffer[, offset])：功能与 recv_bytes() 方法类似，只是该方法将接收到的数据放在 buffer 中。

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