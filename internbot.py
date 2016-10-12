import os
import time
from slackclient import SlackClient
from commands import *
import json

BOT_ID = os.environ.get("SLACK_BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + "* command with numbers, delimited by spaces."
    if command.startswith("add"):
        response = add(command)
    elif command.startswith("help"):
        response = help()

    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                with open('data.txt', 'w') as outfile:
                    json.dump(output, outfile)
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
    return None, None

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")

    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("InternBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
