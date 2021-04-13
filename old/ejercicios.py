# dato = input ('Ingrese Dato: ')
# # print (dato)
# lista = ['Rojo','Negro','Blanco']

# if lista.count(dato) > 0:
#     print ('El dato EXISTE :) ', dato)
# else:
#     print ('El Dato NO EXISTE :( ' , dato)

num1 = input ('Ingrese Primer numero: ')
try: 
    num1 = int(num1)
except:
    num1 = 'texto'

if num1 == 'texto':
    print ('El Primer valor no es Nuemero')
    exit()

num2 = input ('Ingrese Segundo numero: ')
try: 
    num2 = int(num2)
except:
    num2 = 'texto'

if num2 == 'texto':
    print ('El Segundo valor no es Nuemero')
    exit()

simbolo = input('Ingrese Operacion Basica: ') 
if simbolo == '+':
    print('Suma: ', num1 + num2)
elif simbolo =='-':
    print('Resta: ', num1 - num2)
else:
    print ('El Simbolo indicado o es Valido :( ')




    






    
