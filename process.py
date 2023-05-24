from frcnn import FRCNN
import time

import cv2
import numpy as np
from PIL import Image

import os
from tqdm import tqdm
from pathlib import Path
import argparse
import subprocess

from ColorAnalysis import colorAnalysis as ca
from ColorAnalysis import GUI

# call waternet
def call_inference(source_path): # inference.py (WaterNet) 
    # 設定參數
    inference_path = os.path.expanduser("waternet/inference.py")
    output_path = os.path.expanduser("output")
    weights_path = os.path.expanduser("waternet/training/6/last.pt") # 以raw-890訓練的權重

    #使用subprocess.call()來呼叫inference.py程式
    subprocess.call([
       "python3", inference_path,
       "--source", source_path,
       "--name", output_path,
       "--weights", weights_path,
    ])

if __name__ == "__main__":

    # 參數設定
    frcnn = FRCNN()
    #-------------------------------------------------------------------------#
    #   crop                指定了是否在单张图片预测后对目标进行截取
    #   count               指定了是否进行目标的计数
    #   analyze             指定了是否分析色板的色差值 /tana
    #-------------------------------------------------------------------------#
    crop            = True
    count           = False
    analyze         = False
    source_path = os.path.expanduser("input/temp.jpg")

    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str)
    args = parser.parse_args()

    # waternet
    if args.source is None:
        call_inference(source_path)
    else:
        source_path = Path(args.source)
        assert source_path.exists(), f"{args.source} does not exist!"
        call_inference(source_path)
    
    # frcnn
    image = Image.open("waternet/output/output/temp.jpg")
    r_image = frcnn.detect_image(image, crop = crop, analyze = analyze)
    r_image.show()

    # color analysis
    crop_image = Image.open("img_crop/crop_0.png")
    ca.colorAnalysis(crop_image)    
    
    # GUI
    origin = Image.open(source_path)
    restore = Image.open("waternet/output/output/temp.jpg")
    GUI.imageCompare(cv2.cvtColor(np.array(origin),cv2.COLOR_BGR2RGB), cv2.cvtColor(np.array(restore),cv2.COLOR_BGR2RGB), windows_name="Merged Image2")