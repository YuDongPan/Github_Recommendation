# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/23 0:31
import time
import requests
from datetime import datetime

def fetch(url):
    r = requests.get(url)
    print(r.text)


t1 = time.time()
for i in range(100):
    fetch('http://httpbin.org/get')

print("requests版爬虫耗时:", time.time() - t1)