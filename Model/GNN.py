# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/7/9 19:31
import torch
from torch import nn
from torch_geometric.nn import GCNConv
from torch_geometric.nn import global_mean_pool as gmp, global_max_pool as gap
embedding_size = 64

class GCN(nn.Module):
    def __init__(self, num_features):
        # Initialization
        super(GCN, self).__init__()
        torch.manual_seed(42)

        # GCN Layers, transform data features into embedding
        self.initial_conv = GCNConv(num_features, embedding_size)
        self.conv1 = GCNConv(embedding_size, embedding_size)
        self.conv2 = GCNConv(embedding_size, embedding_size)
        self.conv3 = GCNConv(embedding_size, embedding_size)

        # Output layer, a linear layer, transform 128-dimensional vectors to prediction
        self.out = nn.Linear(embedding_size*2, 1)

    def forward(self, x, edge_index, batch_index):
        # 1st Conv Layer
        hidden = self.initial_conv(x, edge_index)
        hidden = torch.tanh(hidden)

        # Other layers
        hidden = self.conv1(hidden, edge_index)
        hidden = torch.tanh(hidden)
        hidden = self.conv2(hidden, edge_index)
        hidden = torch.tanh(hidden)
        hidden = self.conv3(hidden, edge_index)
        hidden = torch.tanh(hidden)

        # Global pooling
        gmp_out = gmp(hidden, batch_index)
        gap_out = gap(hidden, batch_index)

        hidden = torch.cat([gmp_out, gap_out], dim=1)
        out = self.out(hidden)
        return out, hidden








