import json
from urlparse import parse_qs
import random


def parse_roll(command):
    val = random.choice(range(1, 7))
    if command is None:
        return "I rolled one 6 sided dice, and you got: {}".format(val)
    else:
        return ("You asked me to '{}' but I'm too dumb."
                "I rolled you a 6 sided dice and it came up {}").format(command, val)


def handler(event, context):

    with open('.context', 'r') as f:
        gordon_context = json.loads(f.read())

    expected_token = gordon_context['token']

    req_body = event['body']
    params = parse_qs(req_body)

    # Check if the token is the correct one
    token = params['token'][0]
    if token != expected_token:
        raise Exception("Invalid request token")

    # should always be /roll
    # command = params['command'][0]
    command_text = None
    if 'text' in params:
        command_text = params['text'][0]

    roll = parse_roll(command_text)

    response = {
        'response_type': 'in_channel',
        'text': roll,
    }
    return response

# "attachments": [
#    {
#        "text": "This is some extra information!"
#    }
