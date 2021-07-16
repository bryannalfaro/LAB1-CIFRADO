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