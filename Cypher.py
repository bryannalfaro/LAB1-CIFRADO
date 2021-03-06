'''
Universidad del valle de Guatemala
Cifrado de la informacion - laboratorio 1
Integrantes:
Bryann Alfaro
Diego Arredondo
Julio Herrera
'''
from cifrados import *

print('Encriptado caesar:',ECaesar(3,'HOLAMUNDO',alphabet))
caesar = ECaesar(3,'HOLAMUNDO',alphabet)
print('Decriptado caesar:',DCaesar(3,caesar,alphabet))

print('Encriptado afin:',EAfin(5,15,'plantanuclear',alphabet))
afin = EAfin(5,15,'plantanuclear',alphabet)
print('Decriptado afin:',DAfin(5,15,afin,alphabet))


print('Encriptado vigenere:',EVigenere('CRYPTO','HOLAMUNDO',alphabet))
vigenere =EVigenere('CRYPTO','HOLAMUNDO',alphabet)
print('Decriptado vigenere:',DVigenere('CRYPTO',vigenere,alphabet))

file1 = open("cipher1.txt","r",encoding="utf-8")
file1 = file1.read()
print('')

print('')
file2 = open("cipher2.txt","r",encoding="utf-8")
file2 = file2.read()

print('')
file3 = open("cipher3.txt","r", encoding="utf-8")
file3 = file3.read()

print('')

#fuerza bruta
sort = fuerzaC(file1)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
for i in range(1): # Cantidad de posibles claves a mostrar
    print(f'Llave {list(sort.keys())[i]}')
    print(f'error {sort[list(sort.keys())[i]]}%')
    print('Decriptado caesar:',DCaesar(int(list(sort.keys())[i]),file1,alphabet))
    print('')

print('')

sort = fuerzaA(file2)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
for i in range(1): # Cantidad de posibles claves a mostrar
    print(f'Llaves: {list(sort.keys())[i][0]} y {list(sort.keys())[i][1]}')
    print(f'error {sort[list(sort.keys())[i]]}%')
    print('Decriptado afin:',DAfin(list(sort.keys())[i][0],list(sort.keys())[i][1],file2,alphabet))
    print('')

#Se hizo esto ya que el proceso fuerza bruta tarda demasiado en responder y por eso se realiza despues
print('Decriptado Vigenere con llave conocida:',DVigenere('bees',file3,alphabet))
print('')
print('Iniciando fuerza bruta vigenere...\n')
sort = fuerzaV(file3,4)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
for i in range(1): # Cantidad de posibles claves a mostrar
    print(f'Llave: {list(sort.keys())[i]}')
    print(f'error {sort[list(sort.keys())[i]]}%')
    print('Decriptado Vigenere:',DVigenere(list(sort.keys())[i],file3,alphabet))
    print('')
