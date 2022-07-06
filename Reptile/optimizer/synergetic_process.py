# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/23 0:49
import aiohttp
import asyncio
import time


async def fetch(client):
    async with client.get('http://httpbin.org/get') as resp:
        assert resp.status == 200
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)

loop = asyncio.get_event_loop()

tasks = []
for i in range(100):
    task = loop.create_task(main())
    tasks.append(task)

t1 = time.time()
loop.run_until_complete(main())

print("aiohttp版爬虫耗时:", time.time() - t1)