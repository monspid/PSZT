from Formula.Formula import Formula
from Individual.Individual import Individual
from operator import attrgetter
import random
import copy

# rozmiar populacji
size = 10

f = Formula(input('Formula: '))

# slownik do tworzenia osobnikow
temp = dict.fromkeys(f.get_variables())

for x in temp.keys():
	temp[x] = 2

print('temp ', temp)
print(f.get_result(temp))

#tworze populacje
population = list()
children = list()

# generacja populacji początkowej
for i in range(0, size):
	children.append(Individual(f))
	population.append(Individual(f))

population.sort(key = attrgetter('_Individual__value'), reverse = True)

# generacja potomstwa z losowych osobników
for i in range(0, size):
	a = random.randrange(0, size)
	b = random.randrange(0, size)	
	children[i] = Individual(population[a], population[b]) # crossing
	children[i].mutation()

# wybór nowej populacji 
union = population + children
union.sort(key = attrgetter('_Individual__value'), reverse = True)

for x in union:
	print(x)