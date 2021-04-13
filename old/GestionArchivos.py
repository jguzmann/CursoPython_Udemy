# Seccion 11 -> Gestión de Archivos
'''
f = open ('Archivo.txt','w')


read    -> r    : Permiso por defecto lee el archivo
apped   -> a    : Permite ir modificando el archivo pero NO reemplazando completamente su texto si no que ir agragar al final de este mas texto
write   -> w    : Si NO quisieramos ir agragardo texto a este archivo y lo quisierame modificar completamente. Si no existe el archivo esta instruccion lo creara
        -> x    : Si el Archivo no Existe lo crea en el caso que exista Python enviara un ERROR que ya existe.


#print (f.read())       # Lee todas las lineas

print (f.readline())    # Lee una a una las lineas
print (f.readline())
print (f.readline())
print (f.readline())

f.write('\nAgregamos ua nueva linea a nuestro archivo')
f.close()   # Buena practica es cerra el archivo



f = open ('Archivo.txt')

print (f.read())   

for i in f:
    print(i)

f.close()   # Buena practica es cerra el archivo

'''
import os   # Liberia entrega metodos para porder elimonar archivos o carpetas

if os.path.exists ('Archivo.txt'): # Valida si el Archivo Existe
    os.remove ('Archivo.txt')
    print ('Archivo ELIMINADO')
else:
    print ('Archivo NO EXISTE o fue ELIMINADO')

if os.path.exists ('miCarpeta'): # Valida si el Carpeta Existe
    os.rmdir ('miCarpeta')
    print ('Carpeta ELIMINADA')

else:
    print ('Carpeta NO EXISTE o fue ELIMINADO')
