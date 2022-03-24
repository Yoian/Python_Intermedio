from functools import reduce #FUnción reduce importada del módulo functools

#Uso con filter
my_list_filter=[1,4,5,6,9,13,19,21]

odd=list(filter(lambda i: i % 2 !=0, my_list_filter)) 

print(odd)

#Uso de map
my_list_map=[1,2,3,4,5]

squares=list(map(lambda x: x**2, my_list_map))

print(squares)

#Uso de reduce
my_list_reduce=[2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a * b, my_list_reduce)

print(all_multiplied)

