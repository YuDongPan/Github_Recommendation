# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/7/17 22:42
import torch
from torch_geometric.data import InMemoryDataset

class GithubDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(GithubDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_path[0])

    @property
    def raw_file_names(self):
        return ['data_demo.csv']

    @property
    def processed_file_names(self):
        return ['data.pt']

    def process(self):
        pass














