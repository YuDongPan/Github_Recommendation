# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/18 10:32
import towhee
from towhee import pipeline
p = pipeline('image-embedding')
output = p('https://github.com/towhee-io/towhee/blob/main/docs/get-started/towhee.jpeg?raw=true')
print(output)