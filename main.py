from Formula.Formula import Formula
from Individual.Individual import Individual
from operator import attrgetter
import random
import copy

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

number = 0

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
	
	print('population ' + str(number) + '\n')
	print(population[0])

	number += 1
