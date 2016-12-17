import math
from math import * 
import parser
import re

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
			code = re.sub(r'\b%s\b' % key, 'dict[\'' + key + '\']', code)
		return parser.expr(code).compile()

	def get_variables(self):
		return self.__variables

	def set_variables(self, new_variables):
		self.__variables = new_variables

	def get_result(self):
		return eval(self.__code)

f = Formula(input('Formula:'))
dict = f.get_variables()
dict['x'] = 100
f.set_variables(dict)
print(f.get_variables())
print(f.get_result())