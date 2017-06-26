#!/usr/bin/python3

import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMouseEvent
from PyQt5 import QtCore
from PyQt5.QtCore import qDebug, QSize
from random import randint

trueout = sys.stdout

TOAST_WIDTH = 300
TOAST_HEIGHT = 100

class Toast(QWidget):

    def __init__(self, title, body, link):
        super().__init__();
        self.resize(TOAST_WIDTH, TOAST_HEIGHT)
        self.setWindowTitle(title)
        self.setWindowFlags(w.windowFlags() | QtCore.Qt.Tool | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.timerEvent = self.timedOut
        self.mousePressEvent = self.clicked
        self.adjustSize(); 
        label = QLabel(self)
        label.setText(body)
        label.resize(self.size())
        label.show()
        self.startTimer(5000);
        self.move(-TOAST_WIDTH, -TOAST_HEIGHT) # render off screen for geometry calcs to kick in.
        self.show()

    def sizeHint(self):
        return QSize(TOAST_WIDTH, TOAST_HEIGHT)
        
    def timedOut(self, event):
        self.hide()
        self.close()
        self.killTimer(event.timerId())


    def clicked(event):
        sys.exit()   

# def timedOut(event):
#    if len(widgetList) > 0:
#        p = widgetList.pop(0);
#        p.hide()
#        p.close()


class screenManager():
    maxRight = 0
    maxBottom = 0;
    newLoc = (0,0);
    widgetList = [];

    def __init__ (self, desktop):
        self.maxRight = desktop.availableGeometry().right()
        self.maxBottom = desktop.availableGeometry().bottom()
        self.newLoc = ( self.maxRight - TOAST_WIDTH, self.maxBottom - TOAST_HEIGHT )

    def showBox( self, title, body, link):
        p = Toast(title, body, link)
 
        # move into position      
        p.move(self.newLoc[0] - (p.frameGeometry().width() - TOAST_WIDTH), self.newLoc[1] - (p.frameGeometry().height() - TOAST_HEIGHT))
        self.widgetList.append(p)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    qDebug('test Message')

    sm = screenManager(QApplication.desktop());

    w = QWidget()
    w.resize(300, 300)
    w.move(0, 0)
    w.setWindowTitle('Test form')
    w.mousePressEvent = lambda x: sm.showBox("Title", "Body", 0)
    w.show()

    sys.exit(app.exec_())
