alphabet = "abcdefghijklmnñopqrstuvwxyz"
import re
import nltk
import numpy as np
import math
import collections

def limpiar(x):
    contadorTildes = 0
    tildes = ['á','é','í','ó','ú','ã']
    sintildes = ['a','e','i','o','u','']
    caracteres = [' ', '.', ',','(', ')','1', '0', '2', '3', '4', '5', '6', '7', '8', '9',':','?',"-","/","¿","[","]","‘"]
    txt = x.lower() #todas minusculas
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
    decriptado = ''
    x= limpiar(x)

    for w in x:
        letra = (M.find(w)-k) % (len(M))
        decriptado += M[letra]
    return decriptado

#Cifrado afin

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1
#Corregir para validar que sea coprimo
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
    suma = 0
    for i in a:
        suma+= a.get(i) #OBTENER TOTAL

    for i in a:
        a[i]=a.get(i)/suma # PROBABILIDADES

    for i in alphabet:
        if i not in a:
            a[i] = 0 #AGREGAR 0 PARA LETRAS QUE NO ESTEN

    return(a)

#formula seguida: https://ekuatio.com/error-absolutos-y-error-relativos-que-son-y-como-se-calculan/
def metrica(text):
    sumaw = 0
    total = 0
    d = {}
    text=collections.OrderedDict(sorted(text.items()))

    with open("sp_frequencies.txt", encoding="utf-8") as f:
        for line in f:
            (key, val) = line.split('	')
            d[key] = float(val)

    d=collections.OrderedDict(sorted(d.items()))

    for key in d:
        d[key] = (d[key]/100)

    for i in text:
        sumaw +=((d[i] - text[i])**2)
        total +=1

    err = math.sqrt((sumaw)/(total*(total-1)))
    return(err)


def fuerzaC(text):
    dict = {}
    for i in range(len(alphabet)):
        t = DCaesar(i,text,alphabet)
        p = probabilidades(t)
        dict[i]=metrica(p)
    return dict

def fuerzaA(text):
    dict = {}
    for i in range(len(alphabet)):

        for j in range(len(alphabet)):

            t = DAfin((i+1),(j),text,alphabet)
            p = probabilidades(t)
            str = (i+1),(j)
            dict[str]=metrica(p)
    return dict

def fuerzaV(text):
    dict = {}
    arreglo = re.findall('.',alphabet)  #MONOGRAM
    for i in range(len(arreglo)):
        t = DVigenere(arreglo[i],text,alphabet)
        p = probabilidades(t)
        dict[arreglo[i]]=metrica(p)
    return dict
