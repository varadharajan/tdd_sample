import requests

class PublishException(Exception):
	pass

def publish(ticket):
	requests.post('http://awesome-mq.com/')
	return True