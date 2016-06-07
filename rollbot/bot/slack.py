# -*- coding: utf-8 -*-
import json
from urlparse import parse_qs
import dice


def unidice(roll):
    faces = [u'⚀', u'⚁', u'⚂', u'⚃', u'⚄', u'⚅']
    return u' + '.join(faces[x-1] for x in roll)


def parse_roll(command):
    if command is None:
        command = 'd6'
    elif command.strip().lower() == 'help':
        return "`/roll <number>d<sides>`, e.g. `3d20` = 3 20 sided dice."

    try:
        roll = dice.roll(command)
    except:
        return "I'm sorry, I couldn't parse '{}'".format(command)

    if isinstance(roll, int):
        return "{} = {}".format(command, roll)
    if roll.sides <= 6:
        return u"{} = {}".format(unidice(roll), sum(roll))

    return " + ".join(str(x) for x in roll) + " = {}".format(sum(roll))


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
