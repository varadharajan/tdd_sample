import unittest

from mathutils import divide, InvalidArgumentsException

class TestMathUtils(unittest.TestCase):
	def setUp(self):
		print "Setting up things"

	def test_divide_should_divide_two_integers(self):
		self.assertEquals(2, divide(4,2))

	def test_divide_should_raise_exception_if_denominator_is_zero(self):
		with self.assertRaises(InvalidArgumentsException):
			divide(2, 0)

	def test_divide_should_raise_exception_if_operands_are_not_integers(self):
		with self.assertRaises(InvalidArgumentsException):
			divide(1.1, 2)