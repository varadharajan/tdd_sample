import requests

def publish(ticket):
	requests.post('http://awesome-mq.com/')
	return True