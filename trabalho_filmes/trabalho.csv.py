import csv

rt = []
mr = []
yr = []
gr = []
mn = []

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
        mn.append(linha['Movie Name'])
        
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
print("Média do tempo de filme: ", mediart)

mediamr = sum(mr) / len(mr)
print("Média da avaliação: ", mediamr)


#  FILTROS     

indice = 0
contador = 0

for i, y in enumerate(yr):   # filmes do ano de 1950 e com notas acima de 8.0
    if y == 1950 and mr[i] >= 8.0:
        print(f"Título: {titulos[i]} | Ano: {y} | Nota: {mr[i]}")
        contador += 1

        if contador == 10:
            break

contador = 0

for i, m in enumerate(mr):   # filmes com notas acima de 9.0
    if m >= 9.0:          
        print(f"Nome: {mn[i]} | Nota: {m}")
        contador += 1

        if contador == 10:
            break

input_genre = input("Digite um gênero de filme: ").strip().lower()

contador = 0

for i, g in enumerate(gr):   # filmes do gênero digitado pelo usuário
    if input_genre in g.lower():
        print(f"Nome: {mn[i]} | Gênero: {g} |")
        contador += 1
        
        if contador == 10:
            break