import copy
import random
import math

class WrongNumberOfArguments(Exception):
	pass

class Individual():
	def __init__(self, *args):
		# arg[0] = formula
		if(len(args) == 1):
			self.__formula = args[0]
			tempDict = dict.fromkeys(self.__formula.get_variables())
			self.__arguments = tempDict.copy()
			self.__distributions = tempDict.copy()
			self.randomize()
			# self.__value = 0.0
			self.__set_value()
		
		# args[0] = iA, args[1] = iB
		elif(len(args) == 2):
			tempSelf = self.cross(args[0], args[1])
			self.__formula = tempSelf.get_formula()
			self.__arguments = tempSelf.get_arguments()
			self.__distributions  = tempSelf.get_distributions()
			# self.__value = 0.0
			self.__set_value()

		# args[0] = formula, args[1] = arguments, args[2] = distribution
		elif(len(args) == 3):
			self.__formula = args[0]
			self.__arguments = args[1]
			self.__distributions  = args[2]
			# self.__value = 0.0
			self.__set_value()

		else:
			raise WrongNumberOfArguments('Individual() has wrong number of args')

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

	def __set_value(self):
		self.__value = self.__formula.get_result(self.__arguments)

	def get_formula(self):
		return self.__formula

	def cross(self, individualA, individualB):
		if(individualA.get_formula() != individualB.get_formula()):
			raise ValueError("Individual() Individuals have another function")
		
		tempIndividualA = individualA.get_arguments()
		tempIndividualB = individualB.get_arguments()
		keys = tempIndividualA.keys()

		args = (dict.fromkeys(keys)).copy()
		dist = (dict.fromkeys(keys)).copy()

		for x in keys:
			args[x] = (tempIndividualA[x] + tempIndividualB[x]) / 2
		
		# krzyzowanie rozkladow
		tempIndividualA = individualA.get_distributions()
		tempIndividualB = individualB.get_distributions()
		for x in keys:
			dist[x] = (tempIndividualA[x] + tempIndividualB[x]) / 2

		return Individual(individualA.get_formula(), args, dist)

	def mutation(self):
		n = len(self.__arguments)

		xi = random.gauss(0, 1)

		tauPrime = 1 / math.sqrt(2 * n)
		tau = 1 / math.sqrt(2 * math.sqrt(n))

		for key in self.__arguments:
			xi_i =  random.gauss(0, 1)
			self.__arguments[key] = self.__arguments[key] * math.exp(tauPrime * xi + tau * xi_i)

		for key in self.__distributions:
			v_i =  random.gauss(0, 1)
			self.__distributions[key] = self.__distributions[key] + self.__arguments[key] * v_i