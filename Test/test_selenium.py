# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/30 11:04
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

N = 10


edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
s = Service('D:\BrowserDriver\msedgedriver.exe')
browser = webdriver.Edge(service=s, options=edge_options)

start = time.time()
for i in range(N):
    browser.get('https://github.com/ggasdasdasd-----')

    html = browser.page_source
    bf1 = BeautifulSoup(html, 'lxml')
    result = bf1.find_all(class_='Counter')
    print(len(result))
    # print(result[3].text)

end = time.time()
print("cost:", end - start)

# elems = browser.find_elements(By.XPATH, "//span[@class='Counter']")
# elems = browser.find_elements(By.CLASS_NAME, "Counter")


# print([elems[i].text for i in range(len(elems))])
