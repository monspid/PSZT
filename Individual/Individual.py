import copy
import random

class Individual:
	def __init__(self, arguments, distributions):
		self.__arguments = arguments.copy()
		self.__distributions = distributions.copy()
		self.__value = 0.0

	def __str__(self):
		return "arguments: {}\ndistributions: {}\nvalue: {}\n".format(self.__arguments, self.__distributions, self.__value)

	def __repr__(self):
		return self.__str__()

	def randomize(self):
		for x in self.__arguments.keys():
			self.__arguments[x] = random.uniform(-100, 100)
			self.__distributions[x] = random.uniform(-5, 5)

	def __init_distributions(self):
		for x in self.__distributions.keys():
			self.__distributions[x] = random.uniform(-5, 5)

	def get_arguments(self):
		return self.__arguments.copy()
	
	def set_arguments(self, new_variables):
		self.__variables = new_variables.copy()

	def get_distributions(self):
		return self.__distributions.copy()

	def set_distributions(self, new_variables):
		self.__distributions = new_variables.copy()

	def get_value(self):
		return self.__value

	def set_value(self, new_value):
		self.__value = new_value
