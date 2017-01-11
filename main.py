from Formula.Formula import Formula
from Individual.Individual import Individual
import copy
import math
import matplotlib.pyplot as plt
import operator
import random


# Size of population
size = 50
tournametSize = 10

maximizing = input('Type in "min" to look for the minimum (any other input will result in looking for maximum): ')

maximizing = True # delete me after tests

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

while(number <= 10000):
    for i in range(size):
        a = random.randrange(size)
        b = random.randrange(size)
        children[i] = Individual(population[a], population[b]) # crossing
        children[i].mutation()

    union = population + children 
    population = list()
    
    uber = max(union, key = Individual.get_value)
    population.append(uber)
    union.remove(uber)

    while(len(population) != size):
        tournament = random.sample(union, tournametSize)
        winner = max(tournament, key = Individual.get_value)
        population.append(winner)
        union.remove(winner)

    populationNumber.append(number)
    theBestResult.append(round(population[0].get_value(), 4))
    number += 1

    print('number: {} \n{}'.format(number, population[0]))
    
    plt.plot(populationNumber, theBestResult)
    plt.draw()
    plt.pause(10E-200)