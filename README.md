# slackbot-mail-checker
Check my emails and send them to Slack!

## Disclaimer
Super simple and made in a couple of hours, so don't expect much (duplicated code, configuration isn't centralized, security is a mess, plaintext passwords lol).

## Installation

First, add your mail providers' data to the `config_init.py` file.

To configure the bot itself, modify `slack_bot.py` with yout Slack token and the Slack channel where you want to receive the notifications.

Once that's done run on your virtualenv:
```
pip install -r requirements.txt
python config_init.py
python slack_bot.py
```

And you'll be notified about new emails every 5 minutes!
