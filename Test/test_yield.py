# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/17 20:29
def generator():
    for i in range(3):
        # print(i)
        yield i

mygenerator = generator()
for i in mygenerator:
    print(i)

