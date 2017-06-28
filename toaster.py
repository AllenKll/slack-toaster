#!/usr/bin/python3
import os
import sys
import threading
import time
import ScreenManager as sm
from slackclient import SlackClient
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import qDebug, QTimer

import json

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
shutdown = threading.Event()

class myTimer(QTimer):
    manager = None;

    def __init__(self, Manager):
        super().__init__();
        self.manager = Manager
        self.timerEvent = self.callback;

    def callback(self, event):
        new_evts = slack_client.rtm_read()
        for evt in new_evts:
            if "type" in evt:
                if evt["type"] == 'desktop_notification':
                    self.manager.showBox(evt["subtitle"], evt["content"], evt["launchUri"], evt["event_ts"])

if __name__ == '__main__':

    app = QApplication(sys.argv)
    screenMan = sm.ScreenManager(QApplication.desktop());

    # connect up to the slack server
    if slack_client.rtm_connect():
        qDebug ("Connected to RTM")
        # success, start the read thread
        timer = myTimer(screenMan);
        timer.start(1000);
    else:
       qDebug ("No connection to RTM")

    sys.exit(app.exec_())
