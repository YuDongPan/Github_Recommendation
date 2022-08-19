# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/8/19 1:51
import os
import pandas as pd

root = '.'
df_user = pd.read_csv(os.path.join(root, 'users.csv'))
df_project = pd.read_csv(os.path.join(root, 'projects.csv'))
user_dict = df_user['name'].to_dict()
project_dict = df_project['name'].to_dict()

print("user_dict:", user_dict, user_dict[8])
print("project_dict:", project_dict, project_dict[9])