# waternet_fasterRCNN

此專案以深度學習將水下影像還原並分析，結合 waternet 與 Faster R-CNN，分別完成水下影像還原與擷取圖片上的色板，並分析其色彩的差異性。

This project aims to use deep learning to restore and analyze underwater images, combining Waternet and Faster R-CNN to accomplish image restoration and extract color palettes from the images. Additionally, it analyzes the color variations present in the extracted palettes.

功能：
1. 使用 Faster R-CNN 擷取圖片上的色板
2. 使用 Waternet 還原水下影像
3. 使用 Delta E 、色彩通道差的百分比來分析色板的色彩差異性
4. 使用分割的介面，用滑鼠拖動，來比較還原前後的影像

Features:
1. Use Faster R-CNN to extract color palettes from images.
2. Use Waternet to restore underwater images.
3. Use Delta E and the percentage of color channel differences to analyze the color differences in the color palettes.
4. Use the segmentation interface to compare the restored images before and after dragging with the mouse.

<img src="https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/frame9125.jpg?raw=true" alt="frame9125" width="300"><img src="https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/frame9125_waternet.jpg?raw=true" alt="frame9125_waternet" width="300">
<img src="https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/crop3.png?raw=true" alt="crop3" width="300"><img src="https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/crop2.png?raw=true" alt="crop2" width="300">

<img src="https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/delta_e_1.png?raw=true" alt="delta_e_1" width="400">


[report](https://hackmd.io/@tana0101/ai_report) <br>
[bubbliiiing/faster-rcnn-pytorch](https://github.com/bubbliiiing/faster-rcnn-pytorch) <br>
[tnwei/waternet](https://github.com/tnwei/waternet) <br>
[Perspective-control-and-Color-testing](https://github.com/NTOU-Arrays-Start-at-One/Perspective-control-and-Color-testing.git) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15IAx8eKlwPET7O_HTYrmF4C4BVypd9dP?usp=sharing)

## Installation

+ 若要在您的本地端執行此專案，請依照以下步驟進行：

1. 執行以下指令來複製此專案的 repository：
```bash
git clone https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN.git
```

2. 執行以下指令安裝所需的套件：
```bash
pip install -r requirements.txt
```
這個指令會安裝此專案所需的所有套件。

注意：此專案使用的 python 版本為 3.8.10 ，若您的 python 版本差距過大，可能會有套件無法正常使用的問題。

3. 提供權重檔案：
[Google Drive](https://drive.google.com/drive/folders/1wssEZllBeeDrbbDngec0sYgXcW5aBs6Y?usp=drive_link)
Faster R-CNN 權重位置：`warernet_fasterRCNN/logs/ep195-loss0.379-val_loss0.581.pth`
waterNet 預設權重位置：`warernet_fasterRCNN/waternet/training/6/last.pt`
注意：請將兩個權重檔案都放置於對應的位置，在不指定權重位置的情況下，就能夠正常執行。

您也可以使用`process.py --weights WEIGHTS`指定位置，詳細使用請參考下方的 Usage。

<hr>

+ To run this project on your local machine, follow these steps:

1. Clone the repository by running the following command:
```bash
git clone https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN.git
```

2. Install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```
This will install all the necessary packages for this project.

Note: This project uses python version 3.8.10. If your python version is too different, there may be problems with the packages.

3. Provide weight files:
[Google Drive](https://drive.google.com/drive/folders/1wssEZllBeeDrbbDngec0sYgXcW5aBs6Y?usp=drive_link)
  + Faster R-CNN weight location: `warernet_fasterRCNN/logs/ep195-loss0.379-val_loss0.581.pth`
  + waterNet default weight location: `warernet_fasterRCNN/waternet/training/6/last.pt`
  + Note: Please put both weight files in the corresponding locations. If the weight location is not specified, the program will run normally.

You can also use `process.py --weights WEIGHTS` to specify the location. For details, please refer to the Usage below.

## Usage

+ 使用 process.py ：

```bash
usage: process.py [-h] [--source SOURCE] [--weights WEIGHTS]

optional arguments:
  -h, --help         show this help message and exit
  --source SOURCE    Set the image path to be restored
  --weights WEIGHTS  Set the weight path of waternet
```
使用`python process.py --source <image path> --weights <weight path>`，即可將特定影像透過特定的權重還原。

如果不指定位置，則會使用 source: `input/temp.jpg`與 weights: `waternet/training/6/last.pt`。

+ 使用範例：

```bash
python process.py --source input/temp.jpg --weights waternet/training/6/last.pt
```

<hr>

+ Using process.py:

```bash
usage: process.py [-h] [--source SOURCE] [--weights WEIGHTS]

optional arguments:
  -h, --help         show this help message and exit
  --source SOURCE    Set the image path to be restored
  --weights WEIGHTS  Set the weight path of waternet
```

Use `python process.py --source <image path> --weights <weight path>` to restore a specific image with a specific weight.

If the location is not specified, the source: `input/temp.jpg` and weights: `waternet/training/6/last.pt` will be used.

+ Example:

```bash
python process.py --source input/temp.jpg --weights waternet/training/6/last.pt
```

![](https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/unwarp_restored_model%20and%20Standard_image.png?raw=true)
![](https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/delta_e_1.png?raw=true)
![](https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/Histogram%20of%20delta_e.png?raw=true)
![](https://github.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/blob/main/src/crop1.png?raw=true)

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch and make your changes.
3. Push your changes to your forked repository.
4. Create a pull request to merge your changes into the main repository.
