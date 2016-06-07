# Dice Rolling Slackbot

This is toy slackbot to experiment with [gordon](https://gordon.readthedocs.io/).

Gives you a `/roll` command to quickly roll various arrangements of dice. Has a simple syntax:

    /roll help => prints helps
    /roll => rolls a single 6 sided dice
    /roll <number>d<sides> => rolls (number) dice with (sides) sides. 1d6 = 1 six sided dice, 2d20 = 2 20 sided dice.
    /roll <number>d<sides> + <number>d<sides> => you can arbitrarily add different sets, e.g. 1d2 + 3d6 + 10d20

# Creation process notes

    $ pip install gordon
    $ gordon startproject slackroll
    $ cd slackroll
    $ gordon startapp rollbot
    $ export AWS_DEFAULT_PROFILE=myaccount
    ... code
    $ gordon build <-- creates local build artifacts
        $ `make` does a workaround version of this to deal with a homebrew python quirk
    $ gordon apply <-- blasts to aws

I referenced [this](https://github.com/jorgebastida/gordon/blob/master/examples/slack/settings.yml) for a basic slack slash command handler.
