'''
# If y Condiciones
if 2 < 3:
    print ('2 menor que 3')

if 2 == 2:
    print ('2 es igual a 2')

if 7 > 5:
    print ('7 es Mayor a 5')

if 2 !=2:
    print ('2 es distinto que 2') # NO cumple con e If u no imprime

if 2 != 5:
    print ('2 es distinto que 5') # Cumpre con e If u no imprime

if 3 >= 3:
    print('3 es Mayor o Igual que 3')

if 1 <= 2:
    print('1 es Menor o igual que 2')

'''
'''
#  If, elif y else
if 2 > 5:
    print ('2 es Mayor que 5')
elif 2 > 5:
    print ('2 es Menor que 5')
else:
    print('Se imprime solo si lo Anterior NO se cumpre')
'''

'''
# If cortos y ternarios
if 2 < 5: print('If de una sola linea')

print ('Cuando devuelve True') if 5 > 2 else print ('Cuando devuelve False') #Operador Ternario de una sola Linea
'''

# AND y OR
if 2 < 5 and 3 > 2:
    print ('Ambas devuelven True')
    
if 5 < 2 and 3 > 2:
    print ('Hay una False esto no se Mostrara')


if 1 < 0 or 1 > 0:
    print ('Una de las 2 condciones devolvio True')
