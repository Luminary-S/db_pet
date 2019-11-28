#!/usr/bin/venv python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from DBwindow import DBMainWindow
import sys
################################################

################################################
# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setWindowTitle('login in')
#         self.showMaximized()

id_pwd_dict = {"store": "admin",
                "alice":"alice",
                "jack":"jack" }

################################################
################################################
class logindialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(logindialog,self).__init__(*args, **kwargs)
        self.setWindowTitle('login in')
        self.resize(400, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)


        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("ID:")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Password:")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("OK")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("CANCEL")
        self.verticalLayout.addWidget(self.pushButton_quit)

        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_quit.clicked.connect(QCoreApplication.instance().quit)


    def warning_msgbox(self):
        msg = QMessageBox.information(self,
                                "Remind",
                                "Please input right ID and PASSWORD!",
                                QMessageBox.Yes)
        if (msg == QMessageBox.Yes):
            return
        else:
            return


    def on_pushButton_enter_clicked(self):
        account_flag = 0
        pwd_flag = 0
        id = self.lineEdit_account.text()
        pwd = self.lineEdit_password.text()

        if not id_pwd_dict.has_key(id):
            account_flag = 1
        elif not id_pwd_dict.get(id):
            pwd_flag = 1

        # if id == "zjj":
        #     account_flag = 1
        #     # return

      
        # if pwd == "zjj":
        #     pwd_flag = 1
        #     # return
        

        all_flag = pwd_flag + account_flag
    
        print(all_flag)
        if all_flag == 2:
            self.accept()
            # return True
        else:
            self.warning_msgbox()
            return






################################################

################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog()
    if  dialog.exec_()==QDialog.Accepted:
        the_window = DBMainWindow()
        the_window.show()
        sys.exit(app.exec_())
