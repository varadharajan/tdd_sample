import provider
import repository

class InvalidTicketException(Exception):
	pass

class BookingFailureException(Exception):
	pass

class Ticket:
	def __init__(self, name, seat, bus):
		self.__name = name
		self.__seat = seat
		self.__bus = bus

	def valid(self):
		if self.__seat <= 0: raise InvalidTicketException()

		return True

class Service:
	@staticmethod
	def book(ticket):
		assert(ticket.valid() == True)
		try:			
			repository.persist(ticket)
			provider.publish(ticket)
		except: 
			raise BookingFailureException()
		return True