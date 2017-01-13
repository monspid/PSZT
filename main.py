from Formula.Formula import Formula
from Individual.Individual import Individual
import copy
import math
import matplotlib.pyplot as plt
import operator
import random


# Size of population
size = 100
tournametSize = 10

maximizing = input('Type in "min" to look for the minimum (any other input will result in looking for maximum): ')

maxNumber = int(input('Type maximum number of population (default value 2000): ') or "2000")

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
    population.append(Individual(f))

theBestResult = list()
populationNumber = list()
number = 0

plt.xlabel('Population Number')
plt.ylabel('The best result')
plt.ion()

while(number < maxNumber and population[0].get_value() != math.inf and population[0].get_value() != -(math.inf)):
    for i in range(size):
        a = random.randrange(size)
        b = random.randrange(size)
        children[i] = Individual(population[a], population[b]) # crossing
        children[i].mutation()

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


    print('number: {} \n{}'.format(number, population[0]))
    
    if(number % 100 == 0):
        plt.plot(populationNumber, theBestResult)
        plt.draw()
        plt.pause(10E-200)
    
    populationNumber.append(number)
    theBestResult.append(round(population[0].get_value(), 4))
    number += 1

