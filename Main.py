import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTime,QDate
from main_window import Ui_MainWindow
from personalization import Ui_Dialog_personalization
from synchronization import Ui_Dialog_synchronization
# Запуск программы
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui_main = Ui_MainWindow()
ui_main.setupUi(MainWindow)
MainWindow.show()

def openPersonalization(): # функция открытия персонализации
    global Dialog_personalization
    Dialog_personalization = QtWidgets.QDialog()
    pui = Ui_Dialog_personalization()
    pui.setupUi(Dialog_personalization)
    Dialog_personalization.show()
    def saveAndReturnToMainPers(): # сохраняем и возвращаемся на главную
        Dialog_personalization.close()
    pui.pushButton_cust_save.clicked.connect(saveAndReturnToMainPers)
    def cancelAndReturnToMainPers(): # отменяем и возвращаемся на главную
        Dialog_personalization.close()
    pui.pushButton_cust_cancel.clicked.connect(cancelAndReturnToMainPers)

def openSynchronization(): # функция открытия синхронизации
    global Dialog_synchronization
    Dialog_synchronization = QtWidgets.QDialog()
    sui = Ui_Dialog_synchronization()
    sui.setupUi(Dialog_synchronization)
    Dialog_synchronization.show()
    def saveAndReturnToMainSync(): # сохраняем и возвращаемся на главную
        Dialog_synchronization.close()
    sui.pushButton_sync_save.clicked.connect(saveAndReturnToMainSync)
    def cancelAndReturnToMainSync(): # отменяем и возвращаемся на главную
        Dialog_synchronization.close()
    sui.pushButton_sync_cancel.clicked.connect(cancelAndReturnToMainSync)

ui_main.action_custom.triggered.connect(openPersonalization) # открытие персонализации по нажатию
ui_main.action_synchron.triggered.connect(openSynchronization) # открытие синхронизации по нажатию

def setNoteEnabled(): # функция доступа к заметкам
    if ui_main.checkBox_note.isChecked() == True:
        ui_main.textEdit_note.setEnabled(True)
    if ui_main.checkBox_note.isChecked() == False:
        ui_main.textEdit_note.setEnabled(False)
        ui_main.textEdit_note.clear()
ui_main.checkBox_note.stateChanged.connect(setNoteEnabled) # доступ к заметкам

def setRemindEnabled(): # функция доступа к напоминаниям
    if ui_main.checkBox_remind.isChecked() == True:
        ui_main.dateEdit_remind.setEnabled(True)
        ui_main.timeEdit_remind.setEnabled(True)
    if ui_main.checkBox_remind.isChecked() == False:
        ui_main.dateEdit_remind.setEnabled(False)
        ui_main.timeEdit_remind.setEnabled(False)
ui_main.checkBox_remind.stateChanged.connect(setRemindEnabled) # доступ к напоминаниям


sys.exit(app.exec())