#!/usr/bin/python
#Exemplo encrypt e decrypt - Cifra de Cesar
import sys

def encrypt(mensagem):
    cifra = ''
    mensagem = mensagem.lower()
    for letras in mensagem:
        if letras in alfabeto:
            x = alfabeto.find(letras) + chave
            if x >= total:
                x -= total
        cifra += alfabeto[x]
    return cifra

def decrypt(mensagem):
    cifra = ''
    mensagem = mensagem.lower()
    for letras in mensagem:
        if letras in alfabeto:
            x = alfabeto.find(letras) - chave
            cifra += alfabeto[x]
    return cifra
        

if(len(sys.argv) < 4):
    print "[+] Modo de uso: ./cifra.py <chave> <mensagem> <--encrypt>"
    print "[+] Exemplo: ./cifra.py 3 aka --encrypt"
else:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    total = 26
    chave = int(sys.argv[1])
    msg = str(sys.argv[2])

    if "--encrypt" in sys.argv[3]:        
        print "[+] Mensagem: " + encrypt(msg)
    elif "--decrypt" in sys.argv[3]:
        print "[+] Mensagem: " + decrypt(msg) 
