import requests

class PublishException(Exception):
	pass

def publish(ticket):
	try:
		assert(requests.post('http://awesome-mq.com/').status_code == 200)
	except AssertionError:
		raise PublishException()

	return True