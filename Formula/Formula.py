import math
from math import * 
import parser
import re
import copy

class Formula:
	def __init__(self, f):
		self.__formula = f
		self.__variables = self.__init_variables()
		self.__code = self.__init_code()

	def __str__(self):
		return self.__formula
	
	def __repr__(self):
		return self.__str__()

	def __init_variables(self):
		dict = {}
		code = parser.expr(self.__formula).compile()
		for var in code.co_names:
			 if(var not in dir(math)):
			 	dict[var] = 0.0
		return dict

	def __init_code(self):
		code = self.__formula
		for key in self.__variables:
			# change normal variables to the variables which were init in __init_variables
			code = re.sub(r'\b%s\b' % key, 'self.get_variables()[\'' + key + '\']', code)
		return parser.expr(code).compile()

	def get_variables(self):
		return copy.deepcopy(self.__variables)

	def set_variables(self, new_variables):
		self.__variables = copy.deepcopy(new_variables)

	def get_result(self):
		return eval(self.__code)
