# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/7/9 22:04
import torch.nn
import seaborn as sns
import matplotlib.pyplot as plt
from torch_geometric.datasets import MoleculeNet
from rdkit import Chem
from rdkit.Chem import Draw
from Model import GNN
from torch_geometric.loader import DataLoader


# 1.Learn about the molecule dataset

data = MoleculeNet(root='.', name='ESOL')
print(data)

print("Dataset type:", type(data))
print("Dataset features:", data.num_features)
print("Dataset classes:", data.num_classes)
print("Dataset sample:", data[0])
print("Dataset size:", len(data))

# This dataset include 1128 data points, every molecule has 9 attributes, 734 classes

print(data[0].x)
print(data[0].edge_index.T)  # edge_index is used to depict which nodes have edges
print(data[0].y)

print("Dataset sample smiles:", data[0]["smiles"])

# Write molecule equation based on string, and save it into mol.png
molecule = Chem.MolFromSmiles(data[0]['smiles'])
Draw.MolToFile(molecule, 'mol.png')
print(f'Type of molecule: {type(molecule)}')

# 2.Define GCN Architecture
model = GNN.GCN(data.num_features)
model = model.cuda()
print(model)

# 3.Prepare the data
loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

data_size = len(data)
batch_size = 64
train_data = data[:int(data_size * 0.8)]
test_data = data[int(data_size * 0.8):]
train_dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=False)

# 4.Training
train_loss = []
def train(num_epochs, train_iter, test_iter, optimizer, net):
    for epoch in range(num_epochs):
        sum_loss = 0
        for batch in train_iter:
            batch = batch.cuda()
            optimizer.zero_grad()

            pred, embedding = net(batch.x.float(), batch.edge_index, batch.batch)
            loss = torch.sqrt(loss_fn(pred, batch.y))

            loss.backward()
            optimizer.step()

            sum_loss += loss.cpu().data
        epoch_loss = sum_loss / len(train_iter)
        train_loss.append(epoch_loss)

        print(f"Epoch {epoch} | Training loss {epoch_loss}")

        if epoch == num_epochs - 1:
            print(f"Training finish, start testing")
            test_loss = 0.0
            for batch in test_iter:
                batch = batch.cuda()

                pred, _ = net(batch.x.float(), batch.edge_index, batch.batch)
                test_loss += torch.sqrt(loss_fn(pred, batch.y))
                for i in range(len(batch.y)):
                    print(f"y_real:{batch.y[i]}, pred={pred[i]}")

            test_loss = test_loss / len(test_iter)

            print(f"Test finish, test error:{test_loss}")

train(1000, train_dataloader, test_dataloader, optimizer, model)


# 5.Analysis
losses_float = [float(loss) for loss in train_loss]
loss_indices = [i for i, l in enumerate(losses_float)]
sns.lineplot(loss_indices, losses_float)
plt.show()





