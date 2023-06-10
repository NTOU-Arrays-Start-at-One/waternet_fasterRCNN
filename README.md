# waternet_fasterRCNN

此專案以深度學習將水下影像還原並分析，結合 waternet 與 Faster R-CNN，分別完成水下影像還原與擷取圖片上的色板，並分析其色彩的差異性。

This project aims to use deep learning to restore and analyze underwater images, combining Waternet and Faster R-CNN to accomplish image restoration and extract color palettes from the images. Additionally, it analyzes the color variations present in the extracted palettes.

![](https://raw.githubusercontent.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/main/img/0427/frame9125_waternet.jpg?token=GHSAT0AAAAAAB6YHCBA5RHV4OFOP3MS73YQZEEJSLA)

![](https://raw.githubusercontent.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/main/img/frame9125.jpg?token=GHSAT0AAAAAAB6YHCBB3DSD2ATRCVGRHHDAZEEJTAA)

[report](https://hackmd.io/@tana0101/ai_report)
[bubbliiiing/faster-rcnn-pytorch](https://github.com/bubbliiiing/faster-rcnn-pytorch)
[tnwei/waternet](https://github.com/tnwei/waternet)
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
Note: This project uses python version 3.8.10. If your python version is too different, there may be problems with some packages.

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

![](https://raw.githubusercontent.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/main/result/result_20/unwarp_restored_model%20and%20Standard_image.png?token=GHSAT0AAAAAAB6YHCBAPFAW2Z7J3TGNSEOYZEEJUAQ)
![](https://raw.githubusercontent.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/main/result/result_20/Histogram%20of%20delta_e.png?token=GHSAT0AAAAAAB6YHCBAXMRET46NF5YLNKGCZEEJUHA)
![](https://raw.githubusercontent.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/main/result/result_20/delta_e_1.png?token=GHSAT0AAAAAAB6YHCBAT5CTXB664LTEVAE4ZEEJUDQ)

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch and make your changes.
3. Push your changes to your forked repository.
4. Create a pull request to merge your changes into the main repository.
