import os
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from flask import Flask, request
from slack_sdk import WebClient
from slack_bolt import App, Say
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.async_app import AsyncApp

load_dotenv()
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')

client = WebClient(token=SLACK_BOT_TOKEN)
bolt_app = App(token=SLACK_BOT_TOKEN)
signing_secret=os.environ.get("SLACK_SIGNING_SECRET")

@bolt_app.event("app_mention")
def slack_events(body, say):
    print("--------------")
    print(body["event"]["blocks"][0]["elements"][0]["elements"][1]["text"])
    print("--------------")
    say(body["event"]["blocks"][0]["elements"][0]["elements"][1]["text"])

if __name__ == "__main__":
    SocketModeHandler(bolt_app, SLACK_APP_TOKEN).start()