from Formula.Formula import Formula
from Typek.Typek import Typek
from operator import attrgetter
import random
import copy

def krzyzuj(a, b):
        
        temp_a = a.get_arguments()
        temp_b = b.get_arguments()
        keys = temp_a.keys()
        #values = temp_a.values()
        args = copy.deepcopy(dict.fromkeys(keys))
        dist = copy.deepcopy(dict.fromkeys(keys))
        
        for x in keys:
                args[x] = (temp_a[x] + temp_b[x]) / 2
                


        temp_a = a.get_distributions()
        temp_b = b.get_distributions()

        for x in keys:
                dist[x] = (temp_a[x] + temp_b[x]) / 2
        

        return Typek(args, dist)

size = 10

f = Formula(input('Formula: '))

temp = f.get_variables()

print(f.get_variables())

for x in temp.keys():
	temp[x]  = 2

f.set_variables(temp)
print('temp ', temp)
print(f.get_variables())
print(f.get_result())

for x in temp.keys():
	temp[x]  = 1

print('temp ', temp)
print(f.get_variables())
print(f.get_result())


#tworze populacje
population = list();
children = list();
for i in range(0,size):
        children.append(Typek(temp, temp))
        population.append(Typek(temp, temp))
        population[i].randomize()
        f.set_variables(population[i].get_arguments())
        population[i].set_value(f.get_result())       

population.sort(key=attrgetter('_Typek__value'), reverse=True)

for i in range(0, size):
        a = random.randrange(0, size)
        b = random.randrange(0, size)
        #a = 0
        #b = i
        children[i] = krzyzuj(population[a], population[b])

for i in range(0,size):
        f.set_variables(children[i].get_arguments())
        children[i].set_value(f.get_result())

suma = population + children
suma.sort(key=attrgetter('_Typek__value'), reverse=True)
suma = suma[0:size]
print(suma)



