from email_parser import get_latest_mails_bigger_than
from configobj import ConfigObj
from config_init import init_config
from gendo import Gendo

# Your Slack token. Should be in a config file or envvar 
gendo = Gendo('xoxb-xxxxxxxxx-xxxxxxxxxxxxxxxxxx')

# This one should also be there
slack_channel = "mails-and-stuff"


def get_new_emails():
	config = ConfigObj('config.ini')

	for provider, p in config["Accounts"].items():
		mails = get_latest_mails_bigger_than(p["imap_dir"], p["user"], p["pass"], p["latest_id"])

		if len(mails) > 0:
			gendo.speak("New emails at *{0}* ({1})".format(provider, p["link"]), slack_channel)
			gendo.speak('\n'.join(mails), slack_channel)

	init_config()


@gendo.listen_for('check mails')
def check_mails(user, message):
	get_new_emails()


@gendo.cron('*/5 * * * *')
def cron_mails():
	get_new_emails()


if __name__ == '__main__':
	gendo.run()

