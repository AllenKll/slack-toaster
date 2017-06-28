import os
import sys
from slackclient import SlackClient
import threading
import time

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
shutdown = threading.Event()

if __name__ == "__main__":
#test to post message
    slack_client.api_call(
       "chat.postMessage",
       channel="U5Y1C90KF",
       text="Hello PING!"
    )
   

