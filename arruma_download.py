import os
import shutil
import re

lista = []


path = r'C:\Users\Geysson\Downloads' #Endereço da pasta Download no seu computador
diretorios = os.listdir(path)

for arquivo in diretorios:
    sufixo = arquivo[-4:99]
    sufixo2 = arquivo[-5:99]
    if sufixo[0:1] == '.' and not re.findall('[]]', sufixo) and not sufixo.isupper():
        lista.append(sufixo)
    elif sufixo2[0:1] == '.' and not re.findall('[]]', sufixo2) and not sufixo2.isupper():
        lista.append(sufixo)

lista2 = set(lista)
lista3 = list(lista2)
for i in lista3:
    try:
        pathCriar = path + '\\' + i
        os.mkdir(pathCriar)
    except:
        print('Diretorio já existente =>>>>>>>', pathCriar)

for arquivo in diretorios:
    for i in lista3:
        if(arquivo.endswith(i)):
            pathNovo = path + '\\' + i
            pathAntigo = path + '\\' + arquivo
            try:
                shutil.move(pathAntigo, pathNovo)
            except:
                print('--------------------------------------------------------------')
                print('    Arquivo aberto ou já existente =>>>>>>>', arquivo)


try:
    pathCriar2 = path + '\\' + 'Filmes e Séries'
except:
    print('--------------------------------------------------------------')
    print('Diretório Filmes e Séries já criado!')

pathNovo = path + '\\' + 'Filmes e Séries'
for arquivo in diretorios:
    if '1080' in arquivo or '720' in arquivo or 'AC3' in arquivo or 'YTS' in arquivo:
        pathAntigo = path + '\\' + arquivo
        try:
            shutil.move(pathAntigo, pathNovo)
        except:
            print('--------------------------------------------------------------')
            print('    Arquivo aberto ou já existente =>>>>>>>', arquivo)