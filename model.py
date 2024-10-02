from torch import nn
import torch

class Model1(nn.Module):
    def __init__(self, num_layers, layers_with):
        super().__init__()

        self.num_layers = num_layers
        self.layers = []

        for i in range(num_layers + 1):
            if i == 0:
                self.layers.append(nn.Linear(7 * 7, layers_with[i]))
            elif i == num_layers:
                self.layers.append((nn.Linear(layers_with[i - 1], 3)))
            else:
                self.layers.append((nn.Linear(layers_with[i - 1], layers_with[i])))

        self.layers = nn.ModuleList(self.layers)

    def forward(self, data):
        tmp = data
        for layer in self.layers:
            tmp = torch.sigmoid(layer.forward(tmp))
        return tmp
