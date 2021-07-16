alphabet = "abcdefghijklmnñopqrstuvwxyz"

def limpiar(x):
    contadorTildes = 0
    tildes = ['Á','É','í','Ó','Ú']
    sintildes = ['A','E','I','O','U']
    caracteres = [' ', '.', ',','(', ')','1', '0', '2', '3', '4', '5', '6', '7', '8', '9',':','?',"-","/","¿","[","]"]
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