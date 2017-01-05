from Formula.Formula import Formula
from Individual.Individual import Individual
from operator import attrgetter
import random
import copy

# rozmiar populacji
size = 10

f = Formula(input('Formula: '))

# tworze populacje
population = list()
children = list()

# generacja populacji początkowej
for i in range(0, size):
	children.append(Individual(f))
	population.append(Individual(f))

population = sorted(population, key = Individual.get_value, reverse = True)

union = population

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
	print(population[0])

