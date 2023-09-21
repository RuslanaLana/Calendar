from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_synchronization(object):
    def setupUi(self, Dialog_synchronization):
        Dialog_synchronization.setObjectName("Dialog_synchronization")
        Dialog_synchronization.resize(336, 463)
        Dialog_synchronization.setStyleSheet("background-color: rgb(224, 177, 203);\n"
"font: 14pt \"Southbank LT\";")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_synchronization)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_user_service = QtWidgets.QFrame(parent=Dialog_synchronization)
        self.frame_user_service.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(94, 84, 142, 156));\n"
"font: 12pt \"Southbank LT\";\n"
"border-radius:10px;\n"
"color: rgb(35, 25, 66);")
        self.frame_user_service.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_user_service.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_user_service.setObjectName("frame_user_service")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_user_service)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_username = QtWidgets.QLabel(parent=self.frame_user_service)
        self.label_username.setStyleSheet("background-color: none;")
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)
        self.textEdit_username = QtWidgets.QTextEdit(parent=self.frame_user_service)
        self.textEdit_username.setStyleSheet("border-radius:3px;\n"
"background-color: rgb(253, 211, 234);\n"
"border: 1px solid rgb(94, 84, 142);")
        self.textEdit_username.setObjectName("textEdit_username")
        self.verticalLayout.addWidget(self.textEdit_username)
        self.label_password = QtWidgets.QLabel(parent=self.frame_user_service)
        self.label_password.setStyleSheet("background-color: none;")
        self.label_password.setObjectName("label_password")
        self.verticalLayout.addWidget(self.label_password)
        self.textEdit_password = QtWidgets.QTextEdit(parent=self.frame_user_service)
        self.textEdit_password.setStyleSheet("border-radius:3px;\n"
"background-color: rgb(253, 211, 234);\n"
"border: 1px solid rgb(94, 84, 142);")
        self.textEdit_password.setObjectName("textEdit_password")
        self.verticalLayout.addWidget(self.textEdit_password)
        self.horizontalLayout_service = QtWidgets.QHBoxLayout()
        self.horizontalLayout_service.setObjectName("horizontalLayout_service")
        self.label_service = QtWidgets.QLabel(parent=self.frame_user_service)
        self.label_service.setStyleSheet("background-color: none;")
        self.label_service.setObjectName("label_service")
        self.horizontalLayout_service.addWidget(self.label_service)
        self.comboBox_service = QtWidgets.QComboBox(parent=self.frame_user_service)
        self.comboBox_service.setStyleSheet("border-radius:3px;\n"
"background-color: rgb(253, 211, 234);\n"
"border: 1px solid rgb(94, 84, 142);")
        self.comboBox_service.setObjectName("comboBox_service")
        self.comboBox_service.addItem("")
        self.comboBox_service.addItem("")
        self.horizontalLayout_service.addWidget(self.comboBox_service)
        self.verticalLayout.addLayout(self.horizontalLayout_service)
        self.verticalLayout_2.addWidget(self.frame_user_service)
        self.horizontalLayout_sync_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sync_buttons.setObjectName("horizontalLayout_sync_buttons")
        self.pushButton_sync_save = QtWidgets.QPushButton(parent=Dialog_synchronization)
        self.pushButton_sync_save.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 14pt \"Southbank LT\";")
        self.pushButton_sync_save.setObjectName("pushButton_sync_save")
        self.horizontalLayout_sync_buttons.addWidget(self.pushButton_sync_save)
        self.pushButton_sync_cancel = QtWidgets.QPushButton(parent=Dialog_synchronization)
        self.pushButton_sync_cancel.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 14pt \"Southbank LT\";")
        self.pushButton_sync_cancel.setObjectName("pushButton_sync_cancel")
        self.horizontalLayout_sync_buttons.addWidget(self.pushButton_sync_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_sync_buttons)

        self.retranslateUi(Dialog_synchronization)
        QtCore.QMetaObject.connectSlotsByName(Dialog_synchronization)

    def retranslateUi(self, Dialog_synchronization):
        _translate = QtCore.QCoreApplication.translate
        Dialog_synchronization.setWindowTitle(_translate("Dialog_synchronization", "Dialog"))
        self.label_username.setText(_translate("Dialog_synchronization", "Имя пользователя или почта"))
        self.label_password.setText(_translate("Dialog_synchronization", "Пароль"))
        self.label_service.setText(_translate("Dialog_synchronization", "Сервис"))
        self.comboBox_service.setItemText(0, _translate("Dialog_synchronization", "Google"))
        self.comboBox_service.setItemText(1, _translate("Dialog_synchronization", "Яндекс"))
        self.pushButton_sync_save.setText(_translate("Dialog_synchronization", "Сохранить"))
        self.pushButton_sync_cancel.setText(_translate("Dialog_synchronization", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_synchronization = QtWidgets.QDialog()
    ui = Ui_Dialog_synchronization()
    ui.setupUi(Dialog_synchronization)
    Dialog_synchronization.show()
    sys.exit(app.exec())
