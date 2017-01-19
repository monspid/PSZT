import copy
import random
import math

class WrongNumberOfArguments(Exception):
    pass

class Individual():
    def __init__(self, *args):
        # args[0] = formula
        if(len(args) == 1):
            self.__formula = args[0]
            self.randomize()
            self.set_value()
        
        # args[0] = individualA, args[1] = individualB
        elif(len(args) == 2):
            self.cross(args[0], args[1])

        else:
            raise WrongNumberOfArguments('Individual() has wrong number of args')

    def __str__(self):
        return "arguments: {}\ndistributions: {}\nvalue: {}\n".format(self.__arguments, self.__distributions, self.__value)

    def __repr__(self):
        return self.__str__()

    def randomize(self):
        tempDict = dict.fromkeys(self.__formula.get_variables())
        self.__arguments = tempDict.copy()
        self.__distributions = tempDict.copy()
        for x in self.__arguments.keys():
            self.__arguments[x] = random.randrange(-100, 100)
            self.__distributions[x] = random.uniform(25, 200)

    def get_arguments(self):
        return self.__arguments.copy()

    def get_distributions(self):
        return self.__distributions.copy()

    def get_value(self):
        return self.__value

    def set_value(self):
        self.__value = self.__formula.get_result(self.__arguments)

    def get_formula(self):
        return self.__formula

    def cross(self, individualA, individualB):
        if(individualA.get_formula() != individualB.get_formula()):
            raise ValueError("Individual() Individuals have another function")
        
        argumentsA = individualA.get_arguments()
        argumentsB = individualB.get_arguments()

        distributionsA = individualA.get_distributions()
        distributionsB = individualB.get_distributions()

        keys = argumentsA.keys()

        arguments = (dict.fromkeys(keys)).copy()
        distributions = (dict.fromkeys(keys)).copy()

        a = random.uniform(0, 1)
        for x in keys:
            arguments[x] = (a * argumentsA[x] + (1 - a) * argumentsB[x])
            distributions[x] = (a * distributionsA[x] + (1 - a) * distributionsB[x])

        self.__formula = individualA.get_formula()
        self.__arguments = arguments.copy()
        self.__distributions  = distributions.copy()

        self.set_value()


    def mutation(self):
        n = len(self.__arguments)

        if n == 0:
            self.set_value()
            return

        xi = random.gauss(0, 1)

        tauPrime = 1 / math.sqrt(2 * n)
        tau = 1 / math.sqrt(2 * math.sqrt(n))

        for key in self.__arguments:
            xi_i =  random.gauss(0, 1)
            self.__distributions[key] = self.__distributions[key] * math.exp(tauPrime * xi + tau * xi_i)

            v_i =  random.gauss(0, 1)
            self.__arguments[key] = self.__arguments[key] + self.__distributions[key] * v_i

        self.set_value()