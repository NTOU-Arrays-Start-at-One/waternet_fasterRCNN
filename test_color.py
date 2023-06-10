from ColorAnalysis import colorAnalysis as ca
from ColorAnalysis import GUI
from PIL import Image
crop_image = Image.open("img_crop/frame2300.jpg")
ca.colorAnalysis(crop_image)