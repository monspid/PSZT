from Formula.Formula import Formula
from Individual.Individual import Individual
from operator import attrgetter
import random
import copy
import matplotlib.pyplot as plt

# rozmiar populacji
size = 1000

f = Formula(input('Formula: '))

# tworze populacje
population = list()
children = list()

# generacja populacji początkowej
for i in range(size):
	children.append(Individual(f))
	population.append(Individual(f))

population = sorted(population, key = Individual.get_value, reverse = True)

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
		children[i].mutation()

	# wybór nowej populacji 
	union = population + children
	union = sorted(union, key =  Individual.get_value, reverse = True)
	population = union[:size]

	populationNumber.append(number)
	theBestResult.append(round(population[0].get_value(), 4))
	number += 1

	#print(population[0])
	print(round(population[0].get_value(), 4))
	plt.plot(populationNumber, theBestResult)
	plt.draw()
	plt.pause(0.000000001)
