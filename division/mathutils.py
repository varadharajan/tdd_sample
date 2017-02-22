class InvalidArgumentsException(Exception):
	pass

def divide(a, b):

	if not (isinstance(a, int) and isinstance(b, int)): raise InvalidArgumentsException()
	if b == 0 : raise InvalidArgumentsException()

	return a / b