import torch.nn as nn
import torch.nn.functional as F
import torch

def weights_init_normal(m):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        torch.nn.init.normal_(m.weight.data, 0.0, 0.02)
        if hasattr(m, "bias") and m.bias is not None:
            torch.nn.init.constant_(m.bias.data, 0.0)
    elif classname.find("BatchNorm2d") != -1:
        torch.nn.init.normal_(m.weight.data, 1.0, 0.02)
        torch.nn.init.constant_(m.bias.data, 0.0)
        
############generator#############
######2Dencoder+3Ddecoder#########
##### DR:972*768  CT:501*501 #####

class DenseBlock(nn.Module):
    def __init__(self,in_planes,out_planes):
        super(DenseBlock,self).__init__()
        
        
class Encoder(nn.Module):
    def __init__(self,...):
        super(Encoder,self).__init__()
        
        self.basic2d = nn.Sequential(
            nn.Conv2d(1,64,3,padding=1)
            nn.InstanceNorm2d(64)
            nn.ReLU(inplace=True)
            )
        self.
        
        
class Generator(nn.Module):
    def __init__(self,input_shape):
        super(Generator,self).__init__()
        
        
