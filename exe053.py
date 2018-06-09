frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
nfrase = ''.join(frase)
rfrase = str('')
rfrase = nfrase[::-1]
'''for c in range(len(nfrase)-1, -1, -1):
    rfrase += nfrase[c]'''
if rfrase == nfrase:
    print('A frase {} é um palindromo'.format(frase))
else:
    print('A frase {} NÃO é um palindromo'.format(frase))

