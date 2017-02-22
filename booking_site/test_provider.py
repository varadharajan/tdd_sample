from unittest import TestCase
from unittest.mock import patch

from provider import *
from service import Ticket

import requests_mock

class TestProvider(TestCase):


	def test_should_publish_booked_ticket(self):
		ticket = Ticket("varadha", 1, "Bus 1")
		
		with requests_mock.Mocker() as m:
			m.post('http://awesome-mq.com/', json={"status": "ok"})
			self.assertTrue(publish(ticket))
			self.assertTrue(m.called)