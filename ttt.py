import cv2
import numpy as np

img = cv2.imread('img_crop/frame2300.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgbin = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
# 創建結構元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closing = cv2.morphologyEx(imgbin, cv2.MORPH_CLOSE, kernel)
closing = cv2.bitwise_not(closing)
# 連通區域標記
_, labels, _, _ = cv2.connectedComponentsWithStats(closing)

# 取得各個連通區域的統計信息
stats = cv2.connectedComponentsWithStats(closing)
#print(stats)
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

# 尋找輪廓
contours, _ = cv2.findContours(labels, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 找到最大的方形輪廓
max_area = 0
square_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        square_contour = contour

# 提取方形四個點的座標
if square_contour is not None:
    epsilon = 0.1 * cv2.arcLength(square_contour, True)
    approx = cv2.approxPolyDP(square_contour, epsilon, True)
    points = approx.reshape(-1, 2)
    print(points)
    for point in points:
        x, y = point
        cv2.circle(labels, (x, y), 5, (255, 0, 0), -1)

cv2.imshow('test_closing', closing)
cv2.imshow('test_labels', labels)
cv2.waitKey(0)
cv2.destroyAllWindows()