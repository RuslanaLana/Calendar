from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self,parent = None):
        QtWidgets.QCalendarWidget.__init__(self,parent)

    def paintCell(self,painter,rect,date):
        QtWidgets.QCalendarWidget.paintCell(self,painter,rect, date)
        if date == date.currentDate():
            painter.setBrush(QtGui.QColor(94, 84, 142, 60))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawRect(rect)

