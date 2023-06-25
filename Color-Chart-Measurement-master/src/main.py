"""
# @ Color Chart Difference
# @Author  : UAC
# @Time    : 2021/6/15
"""

import sys
from CC_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QImage, QPixmap
import PyQt5.QtCore as QtCore
import cv2
import numpy as np
import os
from imutils.perspective import four_point_transform
import CC_IQA


class MyMainForm(QMainWindow, Ui_MainWindow):
    # 定義一個自定義的信號，用於返回點陣列
    returnPoints = QtCore.pyqtSignal(list)
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.PB_open.clicked.connect(self.open_image)
        self.PB_4points.clicked.connect(self.get_cc_points)
        self.PB_reset.clicked.connect(self.reset)
        self.PB_rot.clicked.connect(self.rot_rect)
        self.PB_cal.clicked.connect(self.cal_diff)
        self.PB_ok.clicked.connect(self.get_scale)
        self.PB_ok_2.clicked.connect(self.return_points)
        self.img_path = ""
        self.cc_points = []
        self.get_p = False
        self.scale = 0.5

    def open_image(self):
        try:
            current_path = os.path.abspath(__file__)
            parent_path = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
            dir_path = os.path.join(parent_path, 'input')
            openfile_name = QFileDialog.getOpenFileName(self, 'select images', dir_path, 'Excel files(*.jpg , *.png)')
            #print(openfile_name)
        except:
            return
        if openfile_name[0] != '':
            self.cc_image.reselect()
            self.img_path = openfile_name[0]
            self.ori_cc_img = cv2.imread(self.img_path)
            self.resize_cc_img = cv2.resize(self.ori_cc_img, (640, 480))
            self.cc_image.show_image(self.resize_cc_img)

    def get_cc_points(self):
        self.get_p = True
        self.cc_points = self.cc_image.return_points(self.ori_cc_img, self.get_p)
        if self.cc_points == False:
            QMessageBox.information(self, 'error', 'The number of selected points is insufficient',
                                    QMessageBox.Ok | QMessageBox.Close,
                                    QMessageBox.Close)
            return
        #print(self.cc_points)
        rect = four_point_transform(self.ori_cc_img.copy(), np.array(self.cc_points))
        #cv2.imwrite("tmp_cc.jpg", rect)
        self.rect_img = cv2.cvtColor(rect.copy(), cv2.COLOR_BGR2RGB)
        self.rect_img = cv2.resize(self.rect_img, (self.area_image.width(), self.area_image.height()))
        self.show_image(self.area_image, self.rect_img, rgb=False)

    def reset(self):
        self.cc_image.reselect()

    def show_image(self, image_label, image, rgb=True):
        # 参数image为np.array类型
        if rgb is True:
            rgb_image = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        else:
            rgb_image = image.copy()
        #rgb_image = cv2.resize(rgb_image, (self.width(), self.height()))
        label_image = QImage(rgb_image.data, rgb_image.shape[1], rgb_image.shape[0], QImage.Format_RGB888)
        image_label.setPixmap(QPixmap.fromImage(label_image))

    def rot_rect(self):
        img = cv2.transpose(self.rect_img)
        img = cv2.flip(img, 0)
        self.rect_img = img.copy()
        self.rect_img = cv2.resize(self.rect_img, (self.area_image.width(), self.area_image.height()))
        self.show_image(self.area_image, self.rect_img, rgb=False)

    def get_scale(self):
        tmp = self.scale_text.text()
        self.scale = float(tmp)

    def return_points(self):
        pts = self.cc_image.return_points(self.ori_cc_img, self.get_p)
        if pts == False:
            QMessageBox.information(self, 'error', 'The number of selected points is insufficient',
                                    QMessageBox.Ok | QMessageBox.Close,
                                    QMessageBox.Close)
            return
        pts = list(map(tuple, pts))
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        output_file = os.path.join(parent_path, "points.txt")
        # 將點陣列寫入輸出檔案
        with open(output_file, 'w') as f:
            f.write(', '.join(str(p) for p in pts))
        #print(pts)
        # 將點陣列作為返回值傳遞給主程式
        self.close()
        self.returnPoints.emit(pts)

    def cal_diff(self):

        m_C, m_E, rect_drawed = CC_IQA.cc_task(self.rect_img, self.scale)
        self.show_image(self.area_image, rect_drawed, rgb=False)
        self.label_C.setText("mean C: {:.4f}".format(m_C))
        self.label_E.setText("mean E: {:.4f}".format(m_E))
    def on_exit_clicked(self):
        QApplication.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    # 設置接收信號的槽函數
    myWin.returnPoints.connect(lambda points: print(points))
    
    myWin.show()
    sys.exit(app.exec_())