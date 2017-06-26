import os
import sys
from slackclient import SlackClient
import threading
import time

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
shutdown = threading.Event()

def readit():

    try:
        while True:
            new_evts = slack_client.rtm_read()
            for evt in new_evts:
                if "type" in evt:
                    if evt["type"] == 'desktop_notification':
                        print( evt["subtitle"] + ": " + evt["content"])

            sys.stdout.flush()
            time.sleep(1)
    finally:
        shutdown.set()

if __name__ == "__main__":
    # connect up to the slack server
    if slack_client.rtm_connect():
        # success, start the read thread
        t = threading.Thread(target=readit, )
        t.daemon = True
        t.start()
    else:
       print ("No connection to RTM")

    # test to post message
    # slack_client.api_call(
    #    "chat.postMessage",
    #    channel="U5Y1C90KF",
    #    text="Hello from Pytssshon! :tada:"
    # )

    shutdown.wait()
   