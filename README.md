# Dice Rolling Slackbot

This is toy slackbot to experiment with [gordon](https://gordon.readthedocs.io/).

# Creation process

    $ pip install gordon
    $ gordon startproject slackroll
    $ cd slackroll
    $ gordon startapp rollbot
    $ export AWS_DEFAULT_PROFILE=myaccount
    ... code
    $ gordon build <-- creates local build artifacts
    $ gordon apply <-- blasts to aws

I referenced [this](https://github.com/jorgebastida/gordon/blob/master/examples/slack/settings.yml) for a basic slack slash command handler.


