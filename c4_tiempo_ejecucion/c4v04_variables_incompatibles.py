var_texto = "Texto"
var_numero = 3
var_decimal = 3.1
var_bool = True

# print(var_texto + var_numero) #Error
print(var_texto * var_numero) #TextoTextoTexto
# print(var_texto * var_decimal) #Error

#Si el booleano es "True" retorna el numero
#Si el booleano es "False" retorna 0
print(var_bool * var_numero) #3

print(var_bool * var_texto) #Texto

#Toma el valore "True" como un 1
print(var_bool + var_numero) #4
