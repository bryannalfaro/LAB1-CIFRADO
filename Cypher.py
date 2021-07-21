'''
Universidad del valle de Guatemala
Cifrado de la informacion - laboratorio 1
Integrantes:
Bryann Alfaro
Diego Arredondo
Julio Herrera


https://es.regionkosice.com/wiki/Affine_cipher
https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
https://www.iteramos.com/pregunta/82300/funcion-inversa-multiplicativa-modular-en-python
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

'''
b) Construir una funci ́on que calcule las distribuci ́on de los caracteres que aparecen en el texto cifrado. Aqu ́ı, por ejemplo, se
pueden usar funciones ya implementadas en NLTK. Sin embargo, se espera que su funci ́on calcule las probabilidades (las
frecuencias divido el total de caracteres). (Sugerencia: Es recomendable completar las letras que no aparezcan en su texto,
con probabilidad 0.)

'''
file1 = open("cipher1.txt","r",encoding="utf-8")
file1 = file1.read()
print('')
#print(probabilidades(file1))
print('')
file2 = open("cipher2.txt","r",encoding="utf-8")
file2 = file2.read()
#print(probabilidades(file2))
print('')
file3 = open("cipher3.txt","r", encoding="utf-8")
file3 = file3.read()
#print(probabilidades(file3))
print('')
#print('Error ',metrica(probabilidades(file3))) #Solo para probar

#fuerza bruta
'''
decriptar, luego calcular prob, luego metrica y guardar en array K, error
'''
sort = fuerzaC(file1)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
print(f'Llave {list(sort.keys())[0]}')
print(f'error {sort[list(sort.keys())[0]]}%')
print('Decriptado caesar:',DCaesar(int(list(sort.keys())[0]),file1,alphabet))

print('')

sort = fuerzaA(file2)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
print(f'Llaves: {list(sort.keys())[0][0]} y {list(sort.keys())[0][1]}')
print(f'error {sort[list(sort.keys())[0]]}%')
print('Decriptado afin:',DAfin(list(sort.keys())[0][0],list(sort.keys())[0][1],file2,alphabet))

'''
sort = fuerzaV(file3)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
print(sort)
print('Decriptado Vigenere:',DVigenere('pqrs',file3,alphabet))

print('')
print('')
'''

print('')

sort = fuerzaV(file3, 6)
sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
print(f'Llave: {list(sort.keys())[0]}')
print(f'Llave: {list(sort.keys())[1]}')
print(f'Llave: {list(sort.keys())[2]}')
print(f'error {sort[list(sort.keys())[0]]}%')
print('Decriptado Vigenere:',DVigenere(list(sort.keys())[0],file3,alphabet))
print('Decriptado Vigenere:',DVigenere(list(sort.keys())[1],file3,alphabet))
print('Decriptado Vigenere:',DVigenere(list(sort.keys())[2],file3,alphabet))