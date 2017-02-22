import provider
import repository

class Ticket:
	def __init__(self, name, seat, bus):
		self.__name = name
		self.__seat = seat
		self.__bus = bus

class Service:
	@staticmethod
	def book(ticket):
		repository.persist(ticket)
		provider.publish(ticket)
		return True