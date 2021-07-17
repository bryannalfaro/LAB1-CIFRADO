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
print('Decriptado caesar:',DCaesar(3,'krñdoxpgr',alphabet))
print('Encriptado afin:',EAfin(1,1,'HOLAMUNDO',alphabet))
print('Decriptado afin:',DAfin(1,1,'ipmbnvñep',alphabet))
print('Encriptado vigenere:',EVigenere('CRYPTO','HOLAMUNDO',alphabet))
print('Decriptado vigenere:',DVigenere('CRYPTO','jgjpfjoun',alphabet))

'''
b) Construir una funci ́on que calcule las distribuci ́on de los caracteres que aparecen en el texto cifrado. Aqu ́ı, por ejemplo, se
pueden usar funciones ya implementadas en NLTK. Sin embargo, se espera que su funci ́on calcule las probabilidades (las
frecuencias divido el total de caracteres). (Sugerencia: Es recomendable completar las letras que no aparezcan en su texto,
con probabilidad 0.)

'''
file1 = open("cipher1.txt","r")
file1 = file1.read()
print(probabilidades(file1))

file2 = open("cipher2.txt","r")
file2 = file2.read()
print(probabilidades(file2))

file3 = open("cipher3.txt","r")
file3 = file3.read()
print(probabilidades(file3))