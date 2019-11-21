import threading
import queue


def consumer(q):
    while True:
        cnt = q.get()

        print('我是消费者',cnt)



def producer(q,cnt):
    while True:
        cnt += 1
        print('我是生产者',cnt)

        q.put(cnt)


if __name__ == '__main__':
    q = queue.Queue()
    cnt = 0
    t1 = threading.Thread(target=producer,args=(q,cnt))
    t2 = threading.Thread(target=consumer,args=(q,cnt))

    t1.start()
    t2.start()

    t1.join()
    t2.join()