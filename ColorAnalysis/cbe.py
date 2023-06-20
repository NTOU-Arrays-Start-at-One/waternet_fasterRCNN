#----------------------------------------------------#
#   cbe.py: ColorBoard Extraction
#   用於將色板提取出來測試
#----------------------------------------------------#

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------邊緣檢測--------------------------------- #

#----------------------------------------------------#
#   find_edge_of_colorboard
#   尋找色板邊緣，用於透視校正。
#----------------------------------------------------#

def find_edge_of_colorboard(im, display=1):
    # cv2.imshow(im)
    img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    imgbin = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
    # 創建結構元素
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closing = cv2.morphologyEx(imgbin, cv2.MORPH_CLOSE, kernel)
    closing = cv2.bitwise_not(closing)
    # 連通區域標記
    _, labels, _, _ = cv2.connectedComponentsWithStats(closing)

    # 取得各個連通區域的統計信息
    stats = cv2.connectedComponentsWithStats(closing)
    # print(stats)
    # 移除面積較小的連通區域
    min_area = 1500  # 設定最小面積閾值
    for label in range(1, stats[0]):
        area = stats[2][label, cv2.CC_STAT_AREA]
        if area < min_area:
            labels[labels == label] = 0
    # 移除背景區域（標籤為 0）
    labels[labels != 0] = 255
    labels = np.uint8(labels)

    labels = cv2.morphologyEx(labels, cv2.MORPH_CLOSE, kernel)
    #labels = cv2.morphologyEx(labels, cv2.MORPH_OPEN, kernel)
    cv2.imshow("orilabels", labels)
    # 尋找輪廓
    contours, _ = cv2.findContours(
        labels, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的方形輪廓
    max_area = 0
    square_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            square_contour = contour

    rect_points = []

    # 提取方形四個點的座標
    if square_contour is not None:
        epsilon = 0.1 * cv2.arcLength(square_contour, True)
        approx = cv2.approxPolyDP(square_contour, epsilon, True)
        points = approx.reshape(-1, 2)
        print(points)
        for point in points:
            x, y = point
            rect_points.append((x, y))
            cv2.circle(labels, (x, y), 5, (255, 0, 0), -1)
    print("rect_points:",rect_points)
    cv2.imshow("prolabels", labels)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 是否顯示結果
    if display == 1:
        cv2.imshow('find_corners', im)
    return rect_points

# ---------------------------------透視校正--------------------------------- #

#----------------------------------------------------#
#   unwarp
#   影像映射、展平。
#----------------------------------------------------#


def unwarp(img, src, dst, display=1):
    h, w = img.shape[:2]
    dstW, dstH = map(int, dst[3])
    # use cv2.getPerspectiveTransform() to get M, the transform matrix, and Minv, the inverse
    M = cv2.getPerspectiveTransform(src, dst)
    # use cv2.warpPerspective() to warp your image to a top-down view
    warped = cv2.warpPerspective(img, M, (dstW, dstH), flags=cv2.INTER_LINEAR)

    if display:
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        f.subplots_adjust(hspace=.2, wspace=.05)
        ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        x = [src[0][0], src[2][0], src[3][0], src[1][0], src[0][0]]
        y = [src[0][1], src[2][1], src[3][1], src[1][1], src[0][1]]
        ax1.plot(x, y, color='red', alpha=0.4, linewidth=3,
                solid_capstyle='round', zorder=2)
        ax1.set_ylim([h, 0])
        ax1.set_xlim([0, w])
        ax1.set_title('Original Image', fontsize=15)
        # ax2.imshow(cv2.flip(warped, 1)) #1:水平翻轉 0:垂直翻轉 -1:水平垂直翻轉
        ax2.imshow(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
        ax2.set_title('Distortion Correction Result', fontsize=15)
        return warped
    else:
        return warped

#----------------------------------------------------#
#   perspective_correction
#   對色板透視校正，將色板抓出。
#----------------------------------------------------#


def perspective_correction(im, rect_point, display=1):
    # 圖片大小
    w, h = im.shape[0], im.shape[1]

    # 頂點(idx由色板右上開始逆時鐘編號)
    # for i in range(0,len(rect_point)):
    #   if(i==4): print()
    #   print(rect_point[i], end='')

    # bug: 可能會因為點的順序錯誤導致透視校正有問題
    # fixed：讓座標能夠(左上，右上，左下，右下)
    # rect_point = sorted(rect_point, key=lambda x: x[0])
    # rect_point = sorted(rect_point, key=lambda x: x[1])
    # rect_point = sorted(rect_point, key=lambda x: x[0], reverse=True)
    # rect_point = sorted(rect_point, key=lambda x: x[1], reverse=True)

    # 座標(左上，右上，左下，右下)
    src = np.float32([(rect_point[2]),
                      (rect_point[3]),
                      (rect_point[0]),
                      (rect_point[1])])

    dst = np.float32([(0, 0),
                      (700, 0),
                      (0, 700),
                      (700, 700)])

    # 校正與輸出
    return unwarp(im, src, dst, display)

# ---------------------------------色板方向校正--------------------------------- #

#----------------------------------------------------#
#   find_rotation_marker
#   利用標準差尋找旋轉用的標記
#----------------------------------------------------#


def find_rotation_marker(img):
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    colorBlockImage = []
    for i in range(0, 2):
        row = []
        for j in range(0, 2):
            # 定義擷取區域的左上角和右下角座標
            x1, y1 = 110 + j*400, 110 + i*400  # 色塊向內縮10pixel
            x2, y2 = 190 + j*400, 190 + i*400
            row.append(im[y1:y2+1, x1:x2+1])
        colorBlockImage.append(row)

    colorBlockStd = []
    for i in range(0, 2):
        row = []
        for j in range(0, 2):
            # 計算標準差
            val_std = np.std(colorBlockImage[i][j])
            colorBlockStd.append({"idx": (i, j), "val_std": val_std})

    # print(colorBlockStd)
    # 找出標準差最大(均勻度最小)的那一個
    max_std = max(colorBlockStd, key=lambda x: x["val_std"])
    # print(max_std["idx"])
    return max_std["idx"]

#----------------------------------------------------#
#   rotate
#   旋轉色板至正確方向
#----------------------------------------------------#


def rotate(colorBoard):
    mark = find_rotation_marker(colorBoard)
    if mark == (0, 0):
        angle = 90
    elif mark == (0, 1):
        angle = 180
    elif mark == (1, 1):
        angle = 270
    else:
        angle = 0

    (h, w, d) = colorBoard.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    colorBoard = cv2.warpAffine(colorBoard, M, (w, h))
    return colorBoard
