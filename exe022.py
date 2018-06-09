nomeComp = str(input('Digite seu nome completo: ')).strip()#Tirar espaços antes e depois
print(nomeComp.upper())
print(nomeComp.lower())
#print(len(nomeComp) - nomeComp.count(' '))
print(len(nomeComp.replace(' ', '')))
divi = nomeComp.split()
print(len(divi[0]))
