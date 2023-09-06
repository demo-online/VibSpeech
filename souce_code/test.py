import os, sys
import argparse
import torch


sys.path.append('/mnt/localDisk1/wangchao/VibSpeech/BigVGAN/')

os.environ['CUDA_VISIBLE_DEVICES'] = '3'
global device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    a = parser.parse_args()

