from Formula.Formula import Formula

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