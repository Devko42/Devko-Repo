"""
### Strings ###

my_string = "Que bobada"
my_other_string = "es esta monda compare"

print (len(my_string))
print (len(my_other_string))

print (my_string + " " + my_other_string)

my_line_string = "Este es un string\nconchesumare" #Con salto de linea
my_tab_string = "\tEste es un string conchesumare tabulado" #Con tabulacion
print (my_line_string)
print (my_tab_string)

name, surname, age = ("Deiver", "Caceres", 25)

print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # ta bien pero nadie lo usa
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # en este se pueden definir los formatos para que age aparezca como numero y no como str
print (f"Mi nombre es {name} {surname} y mi edad es {age}") # el mejor por rapidez
print ("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # este es una mrda

"""
### Desempaquetado de Caracteres ###

language = "python"

a, b, c, d, e, f = language

print (a)
print (e)

xdw = language[1:3]
print (xdw)

xdww = language[0:6:2]
print (xdww)

## Reverso ###

reverso = language[::-1]
print (reverso)

### Funciones ###

print (language.capitalize())
print (language.upper())
print (language.count("t"))
print ("1".isnumeric())
print (language.isnumeric())
print (language.lower())
print (language.lower().isupper())
print (language.startswith("py"))