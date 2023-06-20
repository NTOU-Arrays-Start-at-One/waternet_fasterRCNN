# Color Chart Difference Measurement

## Description
   Measure CIELAB chroma difference and CIELAB color difference by color chart.  
  
## Getting Started

### Run the Demo through Executable File
- UNZIP demo.zip and execute "demo.exe"
- In step 1, click "open" button. Select and open the color chart image to be tested.  
- In step 1, click to select the four corner points of the color chart area on the displayed image. Then click "confirm" button.
- In step 2, the cropped color chart area will be displayed. If it does not correspond to the position of the standard color block , click "Rotate 90" button to adjust it to be consistent with the standard color chart.
- In step 3, after the color blocks are aligned, click "Calculate" button to calculate the indicators. Then results are displayed on the right.

### Note
- Button "reset": reset the selected corner points in the image.
- "block scale"：indicates the area of each color block used for calculation. After setting, you need to click "ok" button. The value should be (0,1].
- For standard color chart, please refer to the display interface.

### Run the Demo through Python Code

#### Install Requriements
- python 3.7
- PyQt5
- opencv-python
- numpy
- scipy

#### Run

	python main.py


# Underwater Image Enhancement Method

## UDCP
[Paper](https://ieeexplore.ieee.org/abstract/document/7426236) & [Code](https://github.com/bilityniu/underwater_dark_chennel)

[1] Paulo LJ Drews, Erickson R Nascimento, Silvia SC Botelho, and Mario Fernando Montenegro Campos, “Underwater depth estimation and image restoration based on single images,” IEEE computer graphics and applications, vol. 36, no. 2, pp. 24–35, 2016.
## RB
[Paper](https://ieeexplore.ieee.org/abstract/document/7025927) & [Code](https://github.com/IsaacChanghau/OptimizedImageEnhance/blob/master/matlab)

[2] Xueyang Fu, Peixian Zhuang, Yue Huang, Yinghao Liao, Xiao-Ping Zhang, and Xinghao Ding, “A retinex-based enhancing approach for single underwater image,” in 2014 IEEE International Conference on Image Processing (ICIP). IEEE, 2014, pp. 4572–4576.
## FB
[Paper](https://ieeexplore.ieee.org/abstract/document/8058463) & [Code](https://github.com/fergaletto/Color-Balance-and-fusion-for-underwater-image-enhancement.-.)

[3] Codruta O Ancuti, Cosmin Ancuti, Christophe De Vleeschouwer, and Philippe Bekaert, “Color balance and fusion for underwater image enhancement,” IEEE Transactions on Image Processing, vol. 27, no. 1, pp. 379–393, 2017.
## UGAN
[Paper](https://ieeexplore.ieee.org/abstract/document/8460552) & [Code](https://github.com/cameronfabbri/Underwater-Color-Correction) or [Code](https://github.com/xahidbuffon/FUnIE-GAN)

[4] Cameron Fabbri, Md Jahidul Islam, and Junaed Sattar, “Enhancing underwater imagery using generative adversarial networks,” in 2018 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2018, pp. 7159–7165.
## Sea-thru
[Paper](https://openaccess.thecvf.com/content_CVPR_2019/html/Akkaynak_Sea-Thru_A_Method_for_Removing_Water_From_Underwater_Images_CVPR_2019_paper.html) & [Code](https://github.com/hainh/sea-thru)

[5] Derya Akkaynak and Tali Treibitz, “Sea-thru: A method for removing water from underwater images,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2019, pp. 1682–1691.
## FUnIEGAN
[Paper](https://ieeexplore.ieee.org/abstract/document/9001231) & [Code](https://github.com/xahidbuffon/FUnIE-GAN)

[6] Md Jahidul Islam, Youya Xia, and Junaed Sattar, “Fast underwater image enhancement for improved visual perception,” IEEE Robotics and Automation Letters, vol. 5, no. 2, pp. 3227–3234, 2020.

# Proposed UICRN demo

Download path: [UICRN_demo](https://github.com/UCV423/Color-Chart-Measurement/releases/tag/UICRN_demo)

## Getting Started
- UNZIP UICRN_demo.zip and execute "./demo/demo.exe"
- Select model from "./pt/UICRN_best.pt"
- Open image from file path
- Run model
