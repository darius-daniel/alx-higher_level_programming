#!/usr/bin/python3

"""A class based upon the one in 6-base_geometry.py
"""


class BaseGeometry:
	"""Adding features to the class defined in 6-base_geometry.py
	"""
	def area(self):
		"""Raises an Exception
		"""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""Validates a value

		Args:
			self: the current instance of the class
			name:  always a string
			value: must be an integer
		"""
		if type(value) is not int:
			raise TypeError("{} must be an integer".format(name))
		elif value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
