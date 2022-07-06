# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/23 0:42
import requests
import time
import multiprocessing
from multiprocessing import Pool


MAX_WORKER_NUM = multiprocessing.cpu_count()
print("MAX_WORKER_NUM:", MAX_WORKER_NUM)


def fetch():
    r = requests.get('http://httpbin.org/get')
    print(r.text)


if __name__ == '__main__':
    t1 = time.time()
    p = Pool(MAX_WORKER_NUM)
    for i in range(100):
        p.apply_async(fetch, args=())
    p.close()
    p.join()

    print('多进程爬虫耗时:', time.time() - t1)

