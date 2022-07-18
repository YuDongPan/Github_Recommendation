# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/7/17 22:42
import pandas as pd
import torch
from torch_geometric.data import InMemoryDataset

class GithubDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(GithubDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_path[0])

    @property
    def num_relations(self):
        return self.data.edge_type.max().item() + 1

    @property
    def num_nodes(self):
        return self.data.x.shape[0]

    @property
    def raw_file_names(self):
        return ['data.csv']

    @property
    def processed_file_names(self):
        return ['data.pt']

    def process(self):
        pass

    def create_df(self, csv_path):
        df = pd.read_csv(csv_path)

        nums = {'user': df.max()['user'] + 1,
                'item': df.max()['project'] + 1,
                'node': df.max()['user'] + df.max()['project'] + 2,
                'edge': len(df)}

        return df, nums

    def create_gt_idx(self, df, nums):
        df['idx'] = df['user'] * nums['project'] + df['project']














