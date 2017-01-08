from Formula.Formula import Formula
from Individual.Individual import Individual
from operator import attrgetter
import random
import copy
import matplotlib.pyplot as plt
import math


def odchylenie(values, srednia):

        sigma = 0.0
        for value in values:
                sigma += ((value - srednia)**2)
        return math.sqrt(sigma / len(values))

def srednia(values):
        suma = 0.0
        suma = sum(values)
        return suma / float(len(values))

_srednia = 0.0
_odchylenie = 0.0
_suma = 0.0


# rozmiar populacji
size = 50


maximizing = input('Type in "min" to look for the minimum (any other input will result in looking for maximum):\n')

if maximizing == 'min':
    maximizing = False
    print('Looking for minimum.\n')
else:
    maximizing = True
    print('Looking for maximum.\n')


f = Formula(input('Formula: '))

# tworze populacje
population = list()
children = [None] * size
values = [None] * 2 * size
ruletka = [None]  * 2 * size
used = [0] * 2 * size

# generacja populacji początkowej
for i in range(size):
    population.append(Individual(f))

population = sorted(population, key = Individual.get_value, reverse = maximizing)

union = population

theBestResult = list()
populationNumber = list()
number = 0

plt.xlabel('Population Number')
plt.ylabel('The best result')
plt.ion()
plt.show()

while(1):
    # generacja potomstwa z losowych osobników
    for i in range(size):
        a = random.randrange(size)
        b = random.randrange(size)
        children[i] = Individual(population[a], population[b]) # crossing
        #children[i] = copy.deepcopy(population[i]) # mutation only
        children[i].mutation()

    # wybór nowej populacji
    union = population + children
    union = sorted(union, key =  Individual.get_value, reverse = maximizing)
    population = union[:size]

###############
    '''
        # ruletka
    for i in range(2 * size):
        values[i] = union[i].get_value()
    _srednia = srednia(values)
    _odchylenie = odchylenie(values, _srednia)
        # normalizacja values
    for i in range(2 * size):
        temp = math.exp((values[i] - _srednia) / _odchylenie)
        values[i] = temp
        # generacja ruletki
    temp = 0.0
    for i in range(2 * size - 1, -1, -1):
        temp += values[i]
        ruletka[i] = temp
    population[0] = union[0]
    max = ruletka[1]
    min = ruletka[2 * size - 1]
    used = [0] * 2 * size
    for i in range(1, size):
        a = random.uniform(min, max)
        #print(a)
        for j in range(1, 2 * size):
            if ruletka[j] < a:
                if used[j-1] == 0:
                    used[j-1] = 1
                    break
        population[i] = union[j - 1]
        #print(population[i])
    #print(values)
    #print(ruletka)
    population = sorted(population, key =  Individual.get_value, reverse = True)
'''
#######################
    populationNumber.append(number)

    theBestResult.append(round(population[0].get_value(), 4))
    number += 1

    if number == 1000:
        break

    #print(population[0])
    #print(round(population[0].get_value(), 4))
    #plt.plot(populationNumber, theBestResult)
    #plt.draw()
    #plt.pause(0.000000001)

print(population)
#print(ruletka)