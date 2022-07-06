# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/23 0:34
import threading
import time
import requests

def fetch(url):
    r = requests.get(url)
    print(r.text)

t1 = time.time()

t_list = []
for i in range(100):
    t = threading.Thread(target=fetch('http://httpbin.org/get'), args=())
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()

print("多线程版爬虫耗时:", time.time() - t1)