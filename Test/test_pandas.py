# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/7/1 22:13
import pandas as pd

df = pd.read_csv('test.csv')

df = df[(df.a >= 3) & (df.a <= 6)]


print("df:", df)