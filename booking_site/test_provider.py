from unittest import TestCase
from unittest.mock import patch

from provider import *
from service import Ticket

class TestProvider(TestCase):
	def test_should_publish_booked_ticket(self):
		ticket = Ticket("varadha", 1, "Bus 1")
		self.assertTrue(publish(ticket))