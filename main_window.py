from PyQt6 import QtCore, QtGui, QtWidgets
from CustomCalendar import  MyCalendar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 540)
        MainWindow.setStyleSheet("background-color: rgb(224, 177, 203);\n"
"font: 12pt \"Southbank LT\";\n"
"color: rgb(35, 25, 66);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget = MyCalendar(parent=self.centralwidget)
        self.calendarWidget.setStyleSheet("font: 22pt \"Southbank LT\";"
"alternate-background-color: rgb(190, 149, 196);\n"
"selection-background-color:rgb(190, 149, 196);\n"
"selection-color: rgb(35, 25, 66);")
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        self.gridLayout_actions = QtWidgets.QGridLayout()
        self.gridLayout_actions.setObjectName("gridLayout_actions")
        self.horizontalLayout_head = QtWidgets.QHBoxLayout()
        self.horizontalLayout_head.setObjectName("horizontalLayout_head")
        self.label_events = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_events.setStyleSheet("font: 16pt \"Southbank LT\";")
        self.label_events.setObjectName("label_events")
        self.horizontalLayout_head.addWidget(self.label_events)
        self.label_date = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_date.setStyleSheet("font: 16pt \"Southbank LT\";")
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_head.addWidget(self.label_date)
        self.gridLayout_actions.addLayout(self.horizontalLayout_head, 0, 0, 1, 1)
        self.verticalLayout_tasks = QtWidgets.QVBoxLayout()
        self.verticalLayout_tasks.setObjectName("verticalLayout_tasks")
        self.label_tasks = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_tasks.setStyleSheet("font: 12pt \"Southbank LT\";\n")
        self.label_tasks.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_tasks.setObjectName("label_tasks")
        self.verticalLayout_tasks.addWidget(self.label_tasks)
        self.table_tasks = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table_tasks.setStyleSheet("background-color: rgb(253, 211, 234);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:3px;\n"
"font: 12pt \"Southbank LT\";")
        self.table_tasks.setObjectName("table_tasks")
        self.verticalLayout_tasks.addWidget(self.table_tasks)
        self.gridLayout_actions.addLayout(self.verticalLayout_tasks, 1, 0, 3, 1)
        self.verticalLayout_nametasks = QtWidgets.QVBoxLayout()
        self.verticalLayout_nametasks.setObjectName("verticalLayout_nametasks")
        self.label_nametasks = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_nametasks.setStyleSheet("font: 12pt \"Southbank LT\";\n")
        self.label_nametasks.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_nametasks.setWordWrap(True)
        self.label_nametasks.setObjectName("label_nametasks")
        self.verticalLayout_nametasks.addWidget(self.label_nametasks)
        self.textEdit_nametasks = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_nametasks.setStyleSheet("background-color: rgb(253, 211, 234);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:5px;\n"
"font: 12pt \"Southbank LT\";")
        self.textEdit_nametasks.setObjectName("textEdit_nametasks")
        self.verticalLayout_nametasks.addWidget(self.textEdit_nametasks)
        self.gridLayout_actions.addLayout(self.verticalLayout_nametasks, 1, 1, 1, 1)
        self.frame_remind = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_remind.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(94, 84, 142, 156));\n"
"font: 12pt \"Southbank LT\";\n"
"border-radius:10px;")
        self.frame_remind.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_remind.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_remind.setObjectName("frame_remind")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_remind)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_remind = QtWidgets.QCheckBox(parent=self.frame_remind)
        self.checkBox_remind.setStyleSheet("background-color: none;\n"
"color: rgb(35, 25, 66);")
        self.checkBox_remind.setObjectName("checkBox_remind")
        self.verticalLayout.addWidget(self.checkBox_remind)
        self.horizontalLayou_date_remind = QtWidgets.QHBoxLayout()
        self.horizontalLayou_date_remind.setObjectName("horizontalLayou_date_remind")
        self.label_date_remind = QtWidgets.QLabel(parent=self.frame_remind)
        self.label_date_remind.setStyleSheet("background-color: none;\n"
"color: rgb(35, 25, 66);")
        self.label_date_remind.setObjectName("label_date_remind")
        self.horizontalLayou_date_remind.addWidget(self.label_date_remind)
        self.dateEdit_remind = QtWidgets.QDateEdit(parent=self.frame_remind)
        self.dateEdit_remind.setEnabled(False)
        self.dateEdit_remind.setStyleSheet("background-color: none;\n"
"border-radius:3px;\n"
"color: rgb(35, 25, 66);")
        self.dateEdit_remind.setObjectName("dateEdit_remind")
        self.horizontalLayou_date_remind.addWidget(self.dateEdit_remind)
        self.verticalLayout.addLayout(self.horizontalLayou_date_remind)
        self.horizontalLayout_time_remind = QtWidgets.QHBoxLayout()
        self.horizontalLayout_time_remind.setObjectName("horizontalLayout_time_remind")
        self.label_time_remind = QtWidgets.QLabel(parent=self.frame_remind)
        self.label_time_remind.setStyleSheet("background-color: none;\n"
"color: rgb(35, 25, 66);")
        self.label_time_remind.setObjectName("label_time_remind")
        self.horizontalLayout_time_remind.addWidget(self.label_time_remind)
        self.timeEdit_remind = QtWidgets.QTimeEdit(parent=self.frame_remind)
        self.timeEdit_remind.setEnabled(False)
        self.timeEdit_remind.setStyleSheet("background-color: none;\n"
"border-radius:3px;\n"
"color: rgb(35, 25, 66);")
        self.timeEdit_remind.setObjectName("timeEdit_remind")
        self.horizontalLayout_time_remind.addWidget(self.timeEdit_remind)
        self.verticalLayout.addLayout(self.horizontalLayout_time_remind)
        self.gridLayout_actions.addWidget(self.frame_remind, 1, 2, 1, 1)
        self.frame_note = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_note.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(94, 84, 142, 156));\n"
"font: 12pt \"Southbank LT\";\n"
"border-radius:10px;")
        self.frame_note.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_note.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_note.setObjectName("frame_note")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_note)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_note = QtWidgets.QCheckBox(parent=self.frame_note)
        self.checkBox_note.setStyleSheet("font: 12pt \"Southbank LT\";\n"
"background-color: none;\n"
"color: rgb(35, 25, 66);")
        self.checkBox_note.setObjectName("checkBox_note")
        self.verticalLayout_2.addWidget(self.checkBox_note)
        self.textEdit_note = QtWidgets.QTextEdit(parent=self.frame_note)
        self.textEdit_note.setEnabled(False)
        self.textEdit_note.setStyleSheet("background-color: rgb(253, 211, 234);\n"
"border: 3px solid rgb(94, 84, 142);\n"
"border-radius:10px;\n"
"font: 12pt \"Southbank LT\";")
        self.textEdit_note.setObjectName("textEdit_note")
        self.verticalLayout_2.addWidget(self.textEdit_note)
        self.gridLayout_actions.addWidget(self.frame_note, 2, 1, 1, 2)
        self.gridLayout_buttons = QtWidgets.QGridLayout()
        self.gridLayout_buttons.setObjectName("gridLayout_buttons")
        self.pushButton_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_save.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 10pt \"Southbank LT\";")
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_buttons.addWidget(self.pushButton_save, 1, 0, 1, 2)
        self.pushButton_close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_close.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 10pt \"Southbank LT\";")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_buttons.addWidget(self.pushButton_close, 1, 2, 1, 1)
        self.pushButton_modify = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_modify.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 10pt \"Southbank LT\";")
        self.pushButton_modify.setObjectName("pushButton_modify")
        self.gridLayout_buttons.addWidget(self.pushButton_modify, 0, 2, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add.setStyleSheet("background-color: rgb(94, 84, 142);\n"
"color: rgb(244, 230, 255);\n"
"border: 1px solid rgb(94, 84, 142);\n"
"border-radius:7px;\n"
"font: 10pt \"Southbank LT\";")
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_buttons.addWidget(self.pushButton_add, 0, 0, 1, 2)
        self.gridLayout_actions.addLayout(self.gridLayout_buttons, 3, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_actions)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 961, 32))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_servise = QtWidgets.QMenu(parent=self.menuBar)
        self.menu_servise.setObjectName("menu_servise")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_custom = QtGui.QAction(parent=MainWindow)
        self.action_custom.setObjectName("action_custom")
        self.action_exit = QtGui.QAction(parent=MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_synchron = QtGui.QAction(parent=MainWindow)
        self.action_synchron.setObjectName("action_synchron")
        self.action_google = QtGui.QAction(parent=MainWindow)
        self.action_google.setObjectName("action_google")
        self.action_yandex = QtGui.QAction(parent=MainWindow)
        self.action_yandex.setObjectName("action_yandex")
        self.menu.addAction(self.action_custom)
        self.menu.addAction(self.action_synchron)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_servise.addAction(self.action_google)
        self.menu_servise.addAction(self.action_yandex)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_servise.menuAction())

        self.retranslateUi(MainWindow)
        # self.action_exit.triggered.connect(MainWindow.close) # type: ignore
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Daily planner"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.label_events.setText(_translate("MainWindow", "События на"))
        self.label_date.setText(_translate("MainWindow", "DATE"))
        self.label_tasks.setText(_translate("MainWindow", "Задачи"))
        self.label_nametasks.setText(_translate("MainWindow", "Наименование задачи"))
        self.checkBox_remind.setText(_translate("MainWindow", "Напоминание"))
        self.label_date_remind.setText(_translate("MainWindow", "Дата"))
        self.label_time_remind.setText(_translate("MainWindow", "Время "))
        self.checkBox_note.setText(_translate("MainWindow", "Заметка"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_close.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_modify.setText(_translate("MainWindow", "Редактировать события"))
        self.pushButton_add.setText(_translate("MainWindow", "Добавить события"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_servise.setTitle(_translate("MainWindow", "Синхронизировать"))
        self.action_custom.setText(_translate("MainWindow", "Персонализация"))
        self.action_exit.setText(_translate("MainWindow", "Выход"))
        self.action_synchron.setText(_translate("MainWindow", "Синхронизация"))
        self.action_google.setText(_translate("MainWindow", "Google"))
        self.action_yandex.setText(_translate("MainWindow", "ЯНДЕКС"))