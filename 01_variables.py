# Variables

string_variable = "ja compae"
print (string_variable)

int_variable = 5
print (int_variable)

bool_variable = True
print (bool_variable)

int_to_str_variable = str(int_variable)
print (int_to_str_variable)
print (type(int_to_str_variable))

# Concadenacion de variables
print (string_variable, int_to_str_variable, bool_variable)
print ("este es el valor de:", bool_variable)

# Algunas funciones del sistema
print (len(string_variable))

# Variables en una sola linea (no abusar)
name, surname, alias, edad = "Deiver", "Caceres", "Devko", 25

print  ("Mi alias es", alias, "mi nombre es", name, surname, "y tengo", edad, "años de edad")

"""
primer_nombre = input("cual es tu nombre culero:")
apellido = input("y el apellido que pendejo?:")

print (primer_nombre)
print (apellido)
"""

address: str = "direccion"

print (type(address))
