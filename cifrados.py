'''
Universidad del Valle de Guatemala
Universidad del valle de Guatemala
Cifrado de la informacion - laboratorio 1
Integrantes:
Bryann Alfaro
Diego Arredondo
Julio Herrera

Some references :
https://es.regionkosice.com/wiki/Affine_cipher
https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
https://www.iteramos.com/pregunta/82300/funcion-inversa-multiplicativa-modular-en-python
'''
import re
import nltk
import math
import itertools
import time

alphabet = "abcdefghijklmnñopqrstuvwxyz"
freqLetrasEspanol = {
    "a": (11.525+0.502), "b": 2.215, "c": 4.019, "d": 5.010, "e": (12.181+0.433), "f": 0.692, "g": 1.768, "h": 0.703, "i": (6.247+0.725), "j": 0.493, "k": 0.011, "l": 4.967,
    "m": 3.157, "n": 6.712, "ñ": 0.311, "o": (8.683+0.827), "p": 2.510, "q": 0.877, "r": 6.871, "s": 7.977, "t": 4.632, "u": (2.927+0.168+0.012), "v": 1.138, "w": 0.017,
    "x": 0.215, "y": 1.008, "z": 0.467
}

def limpiar(x):
    txt = x.lower() #todas minusculas
    contadorTildes = 0
    tildes = ['á','é','í','ó','ú','ã']
    sintildes = ['a','e','i','o','u','']
    caracteres = [' ', '.', ',','(', ')','1', '0', '2', '3', '4', '5', '6', '7', '8', '9',':','?',"-","/","¿","[","]","‘"]
    #Limpiando tildes
    for letra in tildes:
        txt=txt.replace(letra,sintildes[contadorTildes])
        contadorTildes+=1

    #Limpiando caracteres y numeros
    for char in caracteres:
        txt=txt.replace(char,'')

    return txt

#Cifrado Caesar

def ECaesar(k, x, M):
    x = limpiar(x)
    encriptado = ''

    for w in x:
        letra = (M.find(w)+k) % (len(M))
        encriptado += M[letra]
    return encriptado

def DCaesar(k, x, M):
    x = limpiar(x)
    decriptado = ''
    x= limpiar(x)

    for w in x:
        letra = (M.find(w)-k) % (len(M))
        decriptado += M[letra]
    return decriptado

#Cifrado afin
#algoritmo de euclides
#https://altocodigo.blogspot.com/2021/01/maximo-comun-divisor-mcd-en-python.html
def gcd(p,q):
# Crea el gcd de dos numeros.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def EAfin(a,b,x,M):
    if(is_coprime(a,len(M))):
        x = limpiar(x)
        encriptado = ''
        for w in x:

            letra = (a*(M.find(w)+1)+b)%(len(M))

            encriptado += M[letra-1]
        return encriptado
    else:
        return ''

# get from: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return 0
    else:
        return x % m

def DAfin(a,b,x,M):

    if(x !=''):
        decriptado = ''
        x = limpiar(x)
        for w in x:
            h = ((M.find(w)+1)-(b))
            letra = (modinv(a,len(M))*(h))%(len(M))
            decriptado += M[letra-1]
        return decriptado
    else:
        return ''


#Cifrado vigenerep

def EVigenere(k,x, M):
    x = limpiar(x)
    k = limpiar(k)
    encriptado = ''
    contador = 0
    for w in x:
        letra = ((M.find(w))+(M.find(k[contador%(len(k))])))%(len(M))
        encriptado += M[letra]
        contador+=1
    return encriptado

def DVigenere(k,x, M):
    decriptado = ''
    x = limpiar(x)
    contador = 0
    k = limpiar(k)
    for w in x:
        letra = ((M.find(w))-(M.find(k[contador%(len(k))])))%(len(M))
        decriptado += M[letra]
        contador+=1
    return decriptado

#Diccionario de probabilidades
def probabilidades(text):
    text = limpiar(text)
    arreglo = re.findall('.',text)  #MONOGRAMA
    arreglo = nltk.FreqDist(arreglo) # DISTRIBUCION
    a = dict(arreglo) #CONVERTIR DICCIONARIO

    for i in a:
        a[i]=a.get(i)/len(text) # PROBABILIDADES

    for i in alphabet:
        if i not in a:
            a[i] = 0 #AGREGAR 0 PARA LETRAS QUE NO ESTEN

    return(a)

#formula seguida: https://ekuatio.com/error-absolutos-y-error-relativos-que-son-y-como-se-calculan/
def metrica(probs):
    sumaw = 0
    d = {}

    for key in freqLetrasEspanol:
        d[key] = (freqLetrasEspanol[key]/100)

    for i in probs:
        sumaw +=((d[i] - probs[i])**2)

    err = math.sqrt((sumaw)/(len(alphabet)*(len(alphabet)-1)))
    return(err)

def fuerzaC(text):
    start = time.time()
    dict = {}
    for i in range(len(alphabet)):
        t = DCaesar(i,text,alphabet)
        p = probabilidades(t)
        dict[i]=metrica(p)
    stop = time.time()
    print(f'Caesar. Tiempo de ejecución: {stop - start} seconds')
    return dict

def fuerzaA(text):
    start = time.time()
    dict = {}
    for i in range(len(alphabet)):

        for j in range(len(alphabet)):

            t = DAfin((i+1),(j),text,alphabet)
            p = probabilidades(t)
            str = (i+1),(j)
            dict[str]=metrica(p)
    stop = time.time()
    print(f'Afin. Tiempo de ejecución: {stop - start} seconds')
    return dict

def fuerzaV(text,n):
    start = time.time()
    dict = {}
    arreglo = itertools.product(alphabet,repeat=n)
    arreglo = list(arreglo)

    for i in range(len(arreglo)):
        k = "".join(arreglo[i])
        t = DVigenere(k,text,alphabet)
        p = probabilidades(t)
        dict[k]=metrica(p)
    stop = time.time()
    print(f'Vigenere. Tiempo de ejecución: {stop - start} seconds')
    return dict
