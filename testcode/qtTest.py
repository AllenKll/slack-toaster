#!/usr/bin/python3

import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMouseEvent
from PyQt5 import QtCore
from PyQt5.QtCore import qDebug, QSize
from random import randint
import webbrowser

trueout = sys.stdout

TOAST_WIDTH = 300
TOAST_HEIGHT = 100
TOAST_TIMEOUT = 6000
ccc = 1

class Toast(QWidget):
    link = "slack://";
    timer = None;

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
        label.setMargin(10)
        label.show()
        self.link = link
        self.timer = self.startTimer(TOAST_TIMEOUT);
        self.move(-TOAST_WIDTH*2, -TOAST_HEIGHT*2) # render off screen for geometry calcs to kick in.
        self.show()

    def sizeHint(self):
        return QSize(TOAST_WIDTH, TOAST_HEIGHT)
        
    def timedOut(self, event):
        self.hide()
        self.close()
        self.killTimer(self.timer)

    def clicked(self, event):
        webbrowser.open(self.link) 
        self.timedOut(None)


class screenManager():
    maxRight = 0
    maxBottom = 0;
    newLoc = (0,0);
    toastList = [];

    def __init__ (self, desktop):
        self.maxRight = desktop.availableGeometry().right()
        self.maxBottom = desktop.availableGeometry().bottom()
        self.newLoc = ( self.maxRight - TOAST_WIDTH, self.maxBottom - TOAST_HEIGHT )

    def showBox( self, title, body, link):
        p = Toast(title, body, link)
        self.toastList.append(p)

        # clean up toast list
        self.toastList = [ x for x in self.toastList if x.isVisible()]

        # Move all toasts to proper position
        y = self.newLoc[1] - (p.frameGeometry().height() - TOAST_HEIGHT)
        x = self.newLoc[0] - (p.frameGeometry().width() - TOAST_WIDTH)
        for i,toast in enumerate(reversed(self.toastList)):
            if i > 4:
                break;

            toast.move(x, y)
            y = y - p.frameGeometry().height() * 1.1


def testBox(x):
    global ccc
    sm.showBox("Title", str(ccc), "slack://channel?id=D5YNX8K47&message=1498508795972473&team=T5XJYNHNK")
    ccc = ccc + 1

if __name__ == '__main__':

    app = QApplication(sys.argv)
    qDebug('test Message')

    sm = screenManager(QApplication.desktop());

    w = QWidget()
    w.resize(300, 300)
    w.move(0, 0)
    w.setWindowTitle('Test form')
    w.mousePressEvent = testBox
    w.show()

    sys.exit(app.exec_())
