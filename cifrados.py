import re
import nltk
import numpy as np

alphabet = "abcdefghijklmnñopqrstuvwxyz"
freqLetrasEspanol = {
    "a": (11.525+0.502), "b": 2.215, "c": 4.019, "d": 5.010, "e": (12.181+0.433), "f": 0.692, "g": 1.768, "h": 0.703, "i": (6.247+0.725), "j": 0.493, "k": 0.011, "l": 4.967,
    "m": 3.157, "n": 6.712, "ñ": 0.311, "o": (8.683+0.827), "p": 2.510, "q": 0.877, "r": 6.871, "s": 7.977, "t": 4.632, "u": (2.927+0.168+0.012), "v": 1.138, "w": 0.017,
    "x": 0.215, "y": 1.008, "z": 0.467
}

def limpiar(x):
    txt = x.lower() #todas minusculas
    contadorTildes = 0
    tildes = ['á','é','í','ó','ú']
    sintildes = ['a','e','i','o','u']
    caracteres = [' ', '.', ',','(', ')','1', '0', '2', '3', '4', '5', '6', '7', '8', '9',':','?',"-","/","¿","[","]"]
    
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

def metrica(distribution):
    freqSorted = ordenar(freqLetrasEspanol)
    distSorted = ordenar(distribution)
    for i in freqSorted:
        print(i[0],i[1])
    for i in distSorted:
        print(i[0],i[1])

# Order dictionary by values
def ordenar(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

def fuerzaBrutaCaesar(cypher):
    bestKs = {}
    print(cypher)
    prob = probabilidades(cypher)
    for i in range(len(alphabet)):
        desc = DCaesar(i, cypher, alphabet)
        print(i, desc)
    return bestKs