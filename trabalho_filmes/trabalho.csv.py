import csv

rt = []
mr = []
yr = []
gr = []

with open('data.csv', 'r',
          encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    cont = 1
    
    print("Dataset: Filmes")
    print("Nome das colunas: ", leitor.fieldnames)

    for linha in leitor:

        rt.append(int(linha['Run Time in minutes']))
        mr.append(float(linha['Movie Rating']))
        yr.append(int(linha['Year of Release']))
        gr.append(linha['Genre'])

        if cont == 1:
            titulo = linha
        elif cont <= 5:
            print(linha)
        cont += 1

    print("Quantidade de registros: ", cont-1)


#  MIN, MAX e MEDIA     

print("Menor tempo de filme: " , min(rt))
print("Menor avaliação: " , min(mr))

print("Maior tempo de filme: " , max(rt))
print("Maior avaliação: " , max(mr))

mediart = sum(rt) / len(rt)
print(mediart) 

mediamr = sum(mr) / len(mr)
print(mediamr)


#  FILTROS   (fazer + 2)     

indice = 0
for y in yr:
    if y == 1950 and mr[indice] >= 8.0:     # filmes do ano de 1950 e com notas acima de 8.0 
        print(y, mr[indice], indice)
    indice +=1

for m in mr:
    if m >= 5.0:     # filmes com notas acima de 5.0
        print(m, indice)
    indice +=1

for g in gr:
    input_genre = input("Digite um gênero de filme: ")
    if g == input_genre:     # filmes do gênero digitado pelo usuário
        print(g, indice)
    indice +=1
    