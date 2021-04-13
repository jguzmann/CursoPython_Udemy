# Control de Flujo I Parte

# IF y Condiciones


# a   ==  b   # A es IGUAL a B
# a   <   b   # A es MENOR que B
# a   >   b   # A es MAYOR que b
# a   !=  b   # A es DISTINTA que B
# a   <=  b   # A es MENOR o IGUAL que B
# a   >=  b   # A es MAYOR o IGUAL que B

# if 2 < 5:
#     print ('2 es menor que 5 -> OK')

# if 2 == 2:
#     print ('2 es IGUAL que 2 -> OK')

# if 2 == 3:
#     print ('2 es IGUAL que 2')

# if 2 != 2:
#     print ('2 es DISTINTO que 2')

# if 2 != 3:
#     print ('2 es DISTINTO que 3 -> OK')


# if 2 > 3:
#     print ('2 es MAYOR que 3 -> if')
# elif 2 > 3:
#     print ('2 es MENOR que 3 -> elif')
# elif 2 < 3:
#     print ('2 es MENOR que 3 -> Segundo elif')
# else:
#     print ('Se imprime solo si todo lo anterior es faldo')

# If Cortos y Ternarios

# if 2 < 5: print ('if de una sola linea')

# print('Cuando devuelve True') if 5 < 2 else print ('Cuando Devuelve False')

# And y Or
if 2 < 5  and 3 > 2:
    print ('Ambas condiciones devuelven TRUE')

if 2 < 5 and 3 < 2:
    print ('Hay una condicion Falsa, esto no se mostrara')

if 1 < 0 or 1 > 0: 
    print ('Una de las 2 condicion devuelve TRUE')

if 1 < 0 or 1 < 0: 
    print ('Ambas condicion devuelve FALSE, NO se imprimira este PRINT')

