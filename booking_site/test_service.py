from unittest import TestCase
from unittest.mock import patch


from service import Ticket, Service

class TestService(TestCase):

	@patch('provider.publish')
	@patch('repository.persist')
	def test_should_book_tickets_for_user(self, repositoryMock, providerMock):
		repositoryMock.return_value = True
		providerMock.return_value = True

		ticket = Ticket("varadha", "S1", "Bus")

		self.assertTrue(Service.book(ticket))

		repositoryMock.assert_called_with(ticket)
		providerMock.assert_called_with(ticket)