from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_personalization(object):
    def setupUi(self, Dialog_personalization):
        Dialog_personalization.setObjectName("Dialog_personalization")
        Dialog_personalization.resize(367, 132)
        Dialog_personalization.setStyleSheet("background-color: rgb(224, 177, 203)")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_personalization)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_style = QtWidgets.QHBoxLayout()
        self.horizontalLayout_style.setObjectName("horizontalLayout_style")
        self.pushButton_style1 = QtWidgets.QPushButton(parent=Dialog_personalization)
        self.pushButton_style1.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 18pt \"Southbank LT\";")
        self.pushButton_style1.setObjectName("pushButton_style1")
        self.horizontalLayout_style.addWidget(self.pushButton_style1)
        self.pushButton_style2 = QtWidgets.QPushButton(parent=Dialog_personalization)
        self.pushButton_style2.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 18pt \"Southbank LT\";")
        self.pushButton_style2.setObjectName("pushButton_style2")
        self.horizontalLayout_style.addWidget(self.pushButton_style2)
        self.pushButton_style3 = QtWidgets.QPushButton(parent=Dialog_personalization)
        self.pushButton_style3.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 18pt \"Southbank LT\";")
        self.pushButton_style3.setObjectName("pushButton_style3")
        self.horizontalLayout_style.addWidget(self.pushButton_style3)
        self.pushButton_style4 = QtWidgets.QPushButton(parent=Dialog_personalization)
        self.pushButton_style4.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 18pt \"Southbank LT\";")
        self.pushButton_style4.setObjectName("pushButton_style4")
        self.horizontalLayout_style.addWidget(self.pushButton_style4)
        self.verticalLayout.addLayout(self.horizontalLayout_style)
        self.horizontalLayout_save_cancel = QtWidgets.QHBoxLayout()
        self.horizontalLayout_save_cancel.setObjectName("horizontalLayout_save_cancel")
        self.pushButton_cust_save = QtWidgets.QPushButton(parent=Dialog_personalization)
        self.pushButton_cust_save.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 18pt \"Southbank LT\";")
        self.pushButton_cust_save.setObjectName("pushButton_cust_save")
        self.horizontalLayout_save_cancel.addWidget(self.pushButton_cust_save)
        self.pushButton_cust_cancel = QtWidgets.QPushButton(parent=Dialog_personalization)
        self.pushButton_cust_cancel.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 18pt \"Southbank LT\";")
        self.pushButton_cust_cancel.setObjectName("pushButton_cust_cancel")
        self.horizontalLayout_save_cancel.addWidget(self.pushButton_cust_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_save_cancel)

        self.retranslateUi(Dialog_personalization)
        QtCore.QMetaObject.connectSlotsByName(Dialog_personalization)

    def retranslateUi(self, Dialog_personalization):
        _translate = QtCore.QCoreApplication.translate
        Dialog_personalization.setWindowTitle(_translate("Dialog_personalization", "Dialog"))
        self.pushButton_style1.setText(_translate("Dialog_personalization", "Style1"))
        self.pushButton_style2.setText(_translate("Dialog_personalization", "Style2"))
        self.pushButton_style3.setText(_translate("Dialog_personalization", "Style3"))
        self.pushButton_style4.setText(_translate("Dialog_personalization", "Style4"))
        self.pushButton_cust_save.setText(_translate("Dialog_personalization", "Сохранить"))
        self.pushButton_cust_cancel.setText(_translate("Dialog_personalization", "Отмена"))


