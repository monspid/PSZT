import math
from math import * 
import parser
import copy

class Formula():
	def __init__(self, f):
		self.__formula = f
		self.__variables = self.__init_variables()

	def __str__(self):
		return self.__formula
	
	def __repr__(self):
		return self.__str__()

	def __init_variables(self):
		varList = list()
		code = parser.expr(self.__formula).compile()
		for var in code.co_names:
			 if(var not in dir(math)):
			 	varList.append(var)
		return varList

	def get_result(self, varDict):
		code = self.__formula
		for key in self.__variables:
			code = code.replace(key, str(varDict[key]))
		return eval(code)

	def get_variables(self):
		return self.__variables.copy()
