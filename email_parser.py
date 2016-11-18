import imaplib
import email
from email.header import decode_header
from configobj import ConfigObj

config = ConfigObj()

def get_latest_mail_id(imap_dir, username, password):
	mail = imaplib.IMAP4_SSL(imap_dir)
	mail.login(username, password)
	mail.select('inbox')

	result, data = mail.uid('search', None, 'ALL')
	id_list = [int(x) for x in data[0].split()]
	latest = id_list[-1]

	mail.close()
	mail.logout()
	return latest


def get_latest_mails_bigger_than(imap_dir, username, password, id):
	mail = imaplib.IMAP4_SSL(imap_dir)
	mail.login(username, password)
	mail.select('inbox')

	result, data = mail.uid('search', None, 'ALL')
	id_list = [int(x) for x in data[0].split()]
	filtered_list = [x for x in id_list if x > int(id)]
	latest = id_list[-1]

	results = []

	for id in filtered_list:
		result, data = mail.uid('fetch', id, "(RFC822)")
		msg = email.message_from_string(data[0][1])
		_from = decode_header(msg["From"])
		subject = decode_header(msg["Subject"])
		results.append("*{}* sent `{}`".format(_from[0][0], subject[0][0]))

	mail.close()
	mail.logout()
	return results


def get_latest_mail(imap_dir, username, password):
	mail = imaplib.IMAP4_SSL(imap_dir)
	mail.login(username, password)
	mail.select('inbox')

	result, data = mail.uid('search', None, 'ALL')
	id_list = [int(x) for x in data[0].split()]
	latest = id_list[-1]

	result, data = mail.uid('fetch', latest, "(RFC822)")
	msg = email.message_from_string(data[0][1])
	print("'{}' envio '{}'".format(msg["From"], msg["Subject"]))
	mail.close()
	mail.logout()

