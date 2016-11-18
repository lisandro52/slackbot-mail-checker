from configobj import ConfigObj
from email_parser import get_latest_mail_id

def init_config():
	config = ConfigObj()

	config.filename = "config.ini"

	config["Accounts"] = {}

	# You should change these with your own emails
	providers = [{
		'link': 'mail.provider.tld',
		'provider': 'Provider',
		'imap_dir': 'imap.provider.tld',
		'user': 'you@providr.tld',
		'pass': 'secret123'
	}]

	for prov in providers:
		id = get_latest_mail_id(prov['imap_dir'], prov['user'], prov['pass'])
		prov['latest_id'] = id
		config["Cuentas"][prov["provider"]] = prov

	config.write()


if __name__ == '__main__':
	init_config()