import copy
import random

class Typek:
    def __init__(self, args, dist):
        self.__arguments = copy.deepcopy(args)
        self.__distributions = copy.deepcopy(dist)
        self.__value = 0.0

    def __str__(self):
        return "arguments: " + str(self.__arguments) + "\ndistributions: " + str(self.__distributions) + "\nvalue: " + str(self.__value) + "\n"

    def __repr__(self):
        return self.__str__()

    def randomize(self):
        for x in self.__arguments.keys():
            self.__arguments[x] =  random.uniform(-100, 100)
            self.__distributions[x] =  random.uniform(-5, 5)

    def __init_distributions(self):
        for x in self.__distributions.keys():
            self.__distributions[x] =  random.uniform(-5, 5)

    def get_arguments(self):
        return copy.deepcopy(self.__arguments)
    
    def set_arguments(self, new_variables):
        self.__variables = copy.deepcopy(new_variables)

    def get_distributions(self):
        return copy.deepcopy(self.__distributions)

    def set_distributions(self, new_variables):
        self.__distributions = copy.deepcopy(new_variables)

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value


