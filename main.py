from Formula.Formula import Formula
from Individual.Individual import Individual
import copy
import math
import matplotlib.pyplot as plt
import operator
import random
import sys


# Size of population
size = 100
tournametSize = 10

maximizing = input('Type in "min" to look for the minimum (any other input will result in looking for maximum): ')

maxNumber = -1

try:
    maxNumber = int(input('Type maximum number of iterations. Value must be greater than 0 (default value 2000): '))
except ValueError:
    maxNumber = 2000    

if maximizing == 'min':
    maximizing = False
    print('Looking for minimum.\n')
else:
    maximizing = True
    print('Looking for maximum.\n')

f = Formula(input('Formula: '))

population = list()
children = [None] * size

for i in range(size):
    for x in range(10000):    
        try:
            population.append(Individual(f))
            break
        except (ZeroDivisionError, ValueError):
            pass
    else:
        print("Correct Individual was not created")
        sys.exit()
theBestResult = list()
iteration = list()
number = 0

plt.close("all")
plt.xlabel('Iteration')
plt.ylabel('The best result')
plt.xlim([0, maxNumber])
plt.ion()

while(number < maxNumber and population[0].get_value() < 1E307 and population[0].get_value() > -1E307):
    for i in range(size):
        a = random.randrange(size)
        b = random.randrange(size)

        for x in range(10000):    
            try:
                children[i] = Individual(population[a], population[b]) # crossing
                children[i].mutation()
                break
            except (ZeroDivisionError, ValueError):
                pass
        else:
            print("Correct Individual was not created")
            sys.exit()

    union = population + children 
    population = list()
    
    if(maximizing == True):
        uber = max(union, key = Individual.get_value)
    else:
        uber = min(union, key = Individual.get_value)
    
    population.append(uber)
    union.remove(uber)

    while(len(population) != size):
        tournament = random.sample(union, tournametSize)
        if(maximizing == True):
            winner = max(tournament, key = Individual.get_value)
        else:
            winner = min(tournament, key = Individual.get_value)
        population.append(winner)
        union.remove(winner)

    uber = population[0].get_value()
    
    if uber > 1E307:
        uber = 1E307
    elif uber < -1E307:
        uber = -1E307

    theBestResult.append(round(uber, 3))
    iteration.append(number)
    
    print('number: {} \n{}'.format(number, population[0]))

    if(number % 100 == 0):
        plt.plot(iteration, theBestResult)
        plt.draw()
        plt.pause(1E-200)

    number += 1

plt.plot(iteration, theBestResult)
plt.draw()
plt.pause(1E-200)
