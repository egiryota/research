import numpy
import torch
import torchvision
import torch.nn as nn
from torch.nn.functional import relu

class SRCNN(nn.Module):
    def __init__(self):
        super(SRCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=9, padding=4)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=32, kernel_size=1, padding=0)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=3, kernel_size=5, padding=2)

        for m in self.modules():
            if isinstance(m, (nn.Conv2d)):
                nn.init.normal_(m.weight, mean=0, std=0.001)
                nn.init.constant_(m.bias, val=0)

    def forward(self, x):
        x = self.conv1(x)
        x = relu(x)
        x = self.conv2(x)
        x = relu(x)
        x = self.conv3(x)
        return x

class Multiband2dGenerator(nn.Module):
    def __init__(self) -> None:
        super(Multiband2dGenerator, self).__init__()

    def forward(self, x):
        return x


class Encoder(nn.Module):
    def __init__(self) -> None:
        super(Encoder, self).__init__()
        self.relu = nn.ReLU()
        self.pool = nn.MaxPooling2d()

        self.conv1 = nn.Conv2d(1, 512)
        self.conv2 = nn.Conv2d(512, 256)
        self.conv3 = nn.Conv2d(256, 3)

    def forward(self, x):
        return x

class Decoder(nn.Module):
    def __init__(self) -> None:
        super(Decoder, self).__init__()

    def forward(self, x):
        return x
