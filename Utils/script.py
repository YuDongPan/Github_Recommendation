# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/23 12:37
import os
import pandas as pd


def merge_data(filepath, index, fold_num):
    filename_list = os.listdir(filepath)
    print("filename_list:", filename_list)
    csv_list = [pd.read_csv(os.path.join(filepath, filename)) for filename in filename_list if '.csv' in filename]
    df = pd.concat(csv_list)

    df.to_csv(filepath + f'../dataAll/data{index * fold_num + 1}-{(index + 1) * fold_num}.csv', index=False)


def drop_repeat_row(filepath, key):
    df = pd.read_csv(filepath)
    df = df.drop_duplicates(subset=key, keep="first")

    df.to_csv(filepath, index=False)

def split_users(filepath, n_split, fold_num):
    df = pd.read_csv(filepath)

    for i in range(0, n_split):
        filename = f'../github_users/filtered_user{i}-{i + 1}W.csv'
        if i != n_split - 1:
            temp_df = df[(i * fold_num):(i + 1) * fold_num]
        else:
            temp_df = df[i * fold_num:]
        temp_df.to_csv(filename, index=False)