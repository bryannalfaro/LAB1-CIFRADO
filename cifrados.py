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

    for w in x:
        letra = (M.find(w)-k) % (len(M))
        decriptado += M[letra]
    return decriptado

#Cifrado afin

def EAfin(a,b,x,M):
    x = limpiar(x)
    encriptado = ''
    for w in x:
        letra = ((a*M.find(w))+(b))%(len(M))
        encriptado += M[letra]
    return encriptado

def DAfin(a,b,x,M):
    decriptado = ''
    for w in x:
        letra = int(((M.find(w))-(b))/a)%(len(M))
        decriptado += M[letra]
    return decriptado

#Cifrado vigenere

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
    contador = 0
    k = limpiar(k)
    for w in x:
        letra = ((M.find(w))-(M.find(k[contador%(len(k))])))%(len(M))
        decriptado += M[letra]
        contador+=1
    return decriptado

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
        sumaw +=((d[i] - text[i])**2) #aqui se debe reemplazar por la distribucion teorica del español
        total +=1

    err = math.sqrt((sumaw)/(total*(total-1)))
    return(err)