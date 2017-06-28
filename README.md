# toaster
Notification application for Slack.

Requires PyQt5 and slackClient:
```
pip install pyqt5
pip install slackClient
```

run with:
```
nohup python toaster.py &
```
This will run the application in the background.
In order to run you will need to have your auth token set up and set in the environment variable `SLACK_BOT_TOKEN` You can genererat yours here: https://api.slack.com/custom-integrations/legacy-tokens 
