nro1 = input('Ingrese Primer Numero: ')
try:
    nro1 = int(nro1)
except:
    nro1 = 'Numero 1'

if nro1 == 'Numero 1':
    print ('Valor no es un numero')
    exit()

nro2 = input('Ingrese Segundo Numero: ')
try:
    nro2 = int(nro2)
except:
    nro2 = 'Numero 2'

if nro2 == 'Numero 2':
    print ('Valor no es un numero')
    exit()

operacion = input ('Ingrese Operacion Matematica: ')

if operacion == '+':
    print ('La Suma es: ', nro1 + nro2)
elif operacion == '-':
    print ('La Resta es: ', nro1 - nro2)
elif operacion == '*':
    print ('La Multiplicacion es:' , nro1 * nro2)
elif operacion == '/':
    print ('La Division es:' , nro1 / nro2)
else:
    print ('Operacion Matematica NO es Valida')
