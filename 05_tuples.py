### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = ("Deiver", 25, 1.73, "Caceres")
my_other_tuple = (50, 44, 32, 33, 25)

print (my_tuple)
print (type(my_tuple))

print (my_tuple[0])
print (my_tuple[-1])

print (my_tuple.count("Deiver"))
print (my_tuple.index(1.73))

print (my_other_tuple + my_tuple)

my_sume_Tuple = my_tuple + my_other_tuple

print (my_sume_Tuple)
print (my_sume_Tuple [3:6])

my_tuple = list(my_tuple)
print (type(my_tuple))

my_tuple[0] = ("Devko")

print (my_tuple)

my_tuple = tuple(my_tuple)

print (type(my_tuple))
print (my_tuple)