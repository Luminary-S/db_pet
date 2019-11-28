#!/usr/bin/venv python
# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
#project path
import re
# from PROJECTPATH import *
import time
# pyqt5 class
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QFileDialog,QMainWindow, QMessageBox,QStatusBar
from PyQt5 import QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator,QPixmap,QImage
from Ui_DB import Ui_MainWindow
# from ur_gui_ros_node import guiNode

# define class
# from gui_ros_node import *
# import cv2


class DBMainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(DBMainWindow, self).__init__(parent)
        self.setupUi(self)

        # self.setFixedSize(1440,950)
        self.init_show()

    def set_id(self, id):
        self.id = id
        # print(type(self.id))
        # print(self.id)
        str = "Store Holder:  " + self.id + ' ! Welcome to your Pet Management System'
        self.setWindowTitle(  str )

    def init_show(self):
        pass

    # def set_label_pic(self, label, img):
    #     try:
    #         h, w = img.shape[:2]
    #         img = QImage(img,
    #                      w, h, QImage.Format_RGB888)
    #         img = QPixmap.fromImage(img)
    #         label.setPixmap(img)
    #         label.setScaledContents(True)
    #     except:
    #         print("no img for qtgui")

    @pyqtSlot()
    def on_sta_help_btn_clicked(self):
        str =  'In Statistic frame, some important sum, average data can be shown by pressing "obtain".'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_qu_help_btn_clicked(self):
        str = 'In Query frame, through "load", you can load all pets attributes to the combobox; after the chosen of every attribute in the combobox, press "Preview", the pet image can be seen in the Pet Image frame.'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_img_upload_btn_clicked(self):
        # directory = QtWidgets.QFileDialog.getOpenFileName(self,
        #                                                   "getOpenFileName", "./",
        #                                                   "All Files (*)")
        label = self.pet_img_label
        imgName, imgType = QFileDialog.getOpenFileName(self, "open image", "", "*jpeg;;All Files(*);;*.jpg;;*.png")
        jpg = QtGui.QPixmap(imgName).scaled(label.width(), label.height())
        label.setPixmap(jpg)

    @pyqtSlot()
    def on_trans_help_btn_clicked(self):
        str = 'In Transaction frame, you can keep the sell and add record.'
        self.intro_plainTextEdit.setPlainText(str)

    @pyqtSlot()
    def on_img_help_btn_clicked(self):
        str='In Image frame, you can check the pet picture or upload a file to preview.'
        self.intro_plainTextEdit.setPlainText(str)