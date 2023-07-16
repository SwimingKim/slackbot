import os
from dotenv import load_dotenv
from slack_bolt import App, Say
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.async_app import AsyncApp

load_dotenv()
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')
bolt_app = App(token=SLACK_BOT_TOKEN)

@bolt_app.event("app_mention")
def slack_events(body, say):
    say("Hello")
    print(body)

if __name__ == "__main__":
    SocketModeHandler(bolt_app, SLACK_APP_TOKEN).start()