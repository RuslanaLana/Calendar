import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
from main_window import Ui_MainWindow
from personalization import Ui_Dialog_personalization
from synchronization import Ui_Dialog_synchronization

import sqlite3

# Создаем подключение к базе данных
connection = sqlite3.connect('EventsDataBase.db')
сursor = connection.cursor()

# Создаем таблицу Events
сursor.execute('''
CREATE TABLE IF NOT EXISTS Events (
id INTEGER PRIMARY KEY,
eventname TEXT,
date TEXT,
remind TEXT,
note TEXT
)
''')


# # Создаем таблицу Reminds
# сursor.execute('''
# CREATE TABLE IF NOT EXISTS Reminds (
# id INTEGER PRIMARY KEY,
# date TEXT NOT NULL,
# time TEXT NOT NULL
# )
# ''')
#
# # Создаем таблицу Notes
# сursor.execute('''
# CREATE TABLE IF NOT EXISTS Notes (
# id INTEGER PRIMARY KEY,
# textnote TEXT NOT NULL
# )
# ''')


# Объекты главного окна
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
mui = Ui_MainWindow()
mui.setupUi(MainWindow)
MainWindow.show() # Открытие программы
# Объекты окна персонализации
Dialog_personalization = QtWidgets.QDialog()
pui = Ui_Dialog_personalization()
pui.setupUi(Dialog_personalization)
# Объекты окна синхронизации
Dialog_synchronization = QtWidgets.QDialog()
sui = Ui_Dialog_synchronization()
sui.setupUi(Dialog_synchronization)

table = mui.table_tasks

def openPersonalization(): # функция открытия персонализации
    Dialog_personalization.show()
    def saveAndReturnToMainPers(): # сохраняем и возвращаемся на главную
        Dialog_personalization.close()
    pui.pushButton_cust_save.clicked.connect(saveAndReturnToMainPers)
    def cancelAndReturnToMainPers(): # отменяем и возвращаемся на главную
        Dialog_personalization.close()
    pui.pushButton_cust_cancel.clicked.connect(cancelAndReturnToMainPers)
mui.action_custom.triggered.connect(openPersonalization) # открытие персонализации по нажатию

def openSynchronization(): # функция открытия синхронизации
    Dialog_synchronization.show()
    def saveAndReturnToMainSync(): # сохраняем и возвращаемся на главную
        Dialog_synchronization.close()
    sui.pushButton_sync_save.clicked.connect(saveAndReturnToMainSync)
    def cancelAndReturnToMainSync(): # отменяем и возвращаемся на главную
        Dialog_synchronization.close()
    sui.pushButton_sync_cancel.clicked.connect(cancelAndReturnToMainSync)
mui.action_synchron.triggered.connect(openSynchronization) # открытие синхронизации по нажатию

def setNoteEnabled(): # функция доступа к заметкам
    if mui.checkBox_note.isChecked() == True:
        mui.textEdit_note.setEnabled(True)
    if mui.checkBox_note.isChecked() == False:
        mui.textEdit_note.setEnabled(False)
        mui.textEdit_note.clear()
mui.checkBox_note.stateChanged.connect(setNoteEnabled) # доступ к заметкам

def setRemindEnabled(): # функция доступа к напоминаниям
    if mui.checkBox_remind.isChecked() == True:
        mui.dateEdit_remind.setEnabled(True)
        mui.timeEdit_remind.setEnabled(True)
    if mui.checkBox_remind.isChecked() == False:
        mui.dateEdit_remind.setEnabled(False)
        mui.timeEdit_remind.setEnabled(False)
mui.checkBox_remind.stateChanged.connect(setRemindEnabled) # доступ к напоминаниям

def saveEvent(): # функция сохранения события в базу
    name_event = mui.textEdit_nametasks.toPlainText()
    date_event = mui.calendarWidget.selectedDate().toString("dd-MM-yyyy")
    date_remind_event = mui.dateEdit_remind.date().toString("dd-MM-yyyy")
    time_remind_event = mui.timeEdit_remind.time().toString("hh:mm")
    remind_event = date_remind_event + ' ' + time_remind_event
    note_event = mui.textEdit_note.toPlainText()
    сursor.execute('INSERT INTO Events (eventname, date, remind, note) VALUES (?, ?, ?, ?)',(name_event ,date_event,remind_event,note_event))
    connection.commit()
    mui.textEdit_nametasks.clear()
mui.pushButton_add.clicked.connect(saveEvent) #сохранить событие в базу

def watchCurrentEvents(): # функция просмотра текущих событий в таблице
    select_date = mui.calendarWidget.selectedDate().toString("dd-MM-yyyy")
    query = 'SELECT eventname FROM Events WHERE date = ?'
    сursor.execute(query, (select_date,))
    results = сursor.fetchall()
    table.setColumnCount(1)
    table.setColumnWidth(0,mui.calendarWidget.width())
    table.setRowCount(len(results))
    for row in range (len(results)):
        item = QTableWidgetItem(str(results[row][0]))
        table.setItem(row,0,item)
mui.calendarWidget.selectionChanged.connect(watchCurrentEvents) # отразить событие из базы в таблице

def setTaskInEdit(row, column): # функция отображения информации выбранного события
    item = mui.table_tasks.item(row, column)
    if item is not None:
        text = item.text()
    mui.textEdit_nametasks.setText(text)

mui.table_tasks.cellClicked.connect(setTaskInEdit) # отобразить информацию выбранного события



def exitProgramm(): # функция выхода из программы и закрытие соединений
    if Dialog_personalization.isVisible():
        Dialog_personalization.close()
    if Dialog_synchronization.isVisible():
        Dialog_synchronization.close()
    connection.close()
    MainWindow.close()
mui.action_exit.triggered.connect(exitProgramm) # выход из программы

sys.exit(app.exec())