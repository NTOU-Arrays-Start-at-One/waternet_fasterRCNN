# waternet_fasterRCNN

此專案以深度學習將水下影像還原並分析，結合 waternet 與 Faster R-CNN，分別完成水下影像還原與擷取圖片上的色板，並分析其色彩的差異性。

This project aims to use deep learning to restore and analyze underwater images, combining Waternet and Faster R-CNN to accomplish image restoration and extract color palettes from the images. Additionally, it analyzes the color variations present in the extracted palettes.

![](https://raw.githubusercontent.com/NTOU-Arrays-Start-at-One/waternet_fasterRCNN/641aa952c32ddf29d9b7486167c741e74b8f18e0/result/result_18/delta_e_1_unwarp_restored_model.png?token=AXRCWXMAZQMEKDUNBI3YQL3EQRES6)


[report](https://hackmd.io/@tana0101/ai_report)
[bubbliiiing/faster-rcnn-pytorch](https://github.com/bubbliiiing/faster-rcnn-pytorch)
[tnwei/waternet](https://github.com/tnwei/waternet)
[Perspective-control-and-Color-testing](https://github.com/NTOU-Arrays-Start-at-One/Perspective-control-and-Color-testing.git)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15IAx8eKlwPET7O_HTYrmF4C4BVypd9dP?usp=sharing)

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

## Usage

+ 使用 process.py ：

```bash


```

<hr>

+ To use this project, follow these steps:
1. Place the original canvas image in the `src/Original directory` .
2. Place the restored canvas image in the `src/Result_restored directory` .
3. Run `python try.py` to display a comparison of the color difference and results.
4. Upon completion, the text and images will be stored in the `result` directory.

Please follow the above steps to run the program. If you encounter any issues, contact the developers.

![](https://github.com/NTOU-Arrays-Start-at-One/Perspective-control-and-Color-testing/blob/main/result/result/delta_e_1_unwarp_restored_model.png?raw=true)
![](https://github.com/NTOU-Arrays-Start-at-One/Perspective-control-and-Color-testing/blob/main/result/result/delta_e_1.png?raw=true)

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch and make your changes.
3. Push your changes to your forked repository.
4. Create a pull request to merge your changes into the main repository.
