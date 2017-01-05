from Formula.Formula import Formula
from Individual.Individual import Individual
from operator import attrgetter
import random
import copy
import math

def cross(a, b):
	# krzyzowanie argumentow
	temp_a = a.get_arguments()
	temp_b = b.get_arguments()
	keys = temp_a.keys()

	args = (dict.fromkeys(keys)).copy()
	dist = (dict.fromkeys(keys)).copy()

	for x in keys:
		args[x] = (temp_a[x] + temp_b[x]) / 2
	
	# krzyzowanie rozkladow
	temp_a = a.get_distributions()
	temp_b = b.get_distributions()
	for x in keys:
		dist[x] = (temp_a[x] + temp_b[x]) / 2

	return Individual(args, dist)

def mutation(embryo):
	args = embryo.get_arguments()
	dist = embryo.get_distributions()

	n = len(args)

	xi = random.gauss(0, 1)

	tauPrime = 1 / math.sqrt(2 * n)
	tau = 1 / math.sqrt(2 * math.sqrt(n))

	for key in args:
		xi_i =  random.gauss(0, 1)
		args[key] = args[key] * math.exp(tauPrime * xi + tau * xi_i)

	for key in dist:
		v_i =  random.gauss(0, 1)
		dist[key] = dist[key] + args[key] * v_i
	embryo.set_arguments(args)
	embryo.set_distributions(dist)

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
population = list();
children = list();

# generacja populacji początkowej
for i in range(0, size):
	children.append(Individual(temp, temp))
	population.append(Individual(temp, temp))
	population[i].randomize()
	population[i].set_value(f.get_result(population[i].get_arguments()))

population.sort(key = attrgetter('_Individual__value'), reverse = True)

# generacja potomstwa z losowych osobników
for i in range(0, size):
	a = random.randrange(0, size)
	b = random.randrange(0, size)	
	children[i] = cross(population[a], population[b])
	mutation(children[i])

# obliczenie wartosci funkcji celu dla potomstwa
for i in range(0, size):
	children[i].set_value(f.get_result(children[i].get_arguments()))

# wybór nowej populacji 
union = population + children
union.sort(key = attrgetter('_Individual__value'), reverse = True)

for x in union:
	print(x)
