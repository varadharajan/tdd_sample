from unittest import TestCase
from unittest.mock import patch


from service import *

class TestService(TestCase):

	@patch('provider.publish')
	@patch('repository.persist')
	def test_should_book_tickets_for_user(self, repositoryMock, providerMock):
		ticket = Ticket("varadha", 1, "Bus")

		self.assertTrue(Service.book(ticket))

		repositoryMock.assert_called_with(ticket)
		providerMock.assert_called_with(ticket)

	def test_should_raise_exception_if_ticket_details_are_invalid(self):
		ticket = Ticket("varadha", -100, "Bus")
		with self.assertRaises(InvalidTicketException):
			Service.book(ticket)

	@patch('provider.publish')
	@patch('repository.persist')	
	def test_should_raise_exception_if_persist_to_repository_fails(self, repositoryMock, providerMock):
		repositoryMock.side_effect = Exception("Persist to repository failed")

		ticket = Ticket("varadha", 1, "Bus")

		with self.assertRaises(BookingFailureException):
			Service.book(ticket)

		self.assertFalse(providerMock.called)


	@patch('provider.publish')
	@patch('repository.persist')	
	def test_should_raise_exception_if_publish_fails(self, repositoryMock, providerMock):
		providerMock.side_effect = Exception("Public failed")

		ticket = Ticket("varadha", 1, "Bus")

		with self.assertRaises(BookingFailureException):
			Service.book(ticket)

		self.assertTrue(repositoryMock.called)



class TestTicket(TestCase):
	def test_should_validate_tickets(self):
		ticket = Ticket("varadha", 10, "Bus 1")
		self.assertTrue(ticket.valid())

	def test_raise_exception_if_ticket_is_invalid(self):
		ticket = Ticket("varadha", -1, "Bus 2")
		with self.assertRaises(InvalidTicketException):
			ticket.valid()