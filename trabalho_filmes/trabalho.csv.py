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

for i, y in enumerate(yr):   # filmes do ano de 2000 e com notas acima de 8.0
    if y == 2000 and mr[i] >= 8.0:
        print(f"Ano: {y} | Nota: {mr[i]} | Nome: {mn[i]} |")
        contador += 1

        if contador == 10:
            break

contador = 0

for i, m in enumerate(mr):   # filmes com notas acima de 9.0
    if m >= 9.0:          
        print(f"Nota: {m} | Nome: {mn[i]} |")
        contador += 1

        if contador == 10:
            break

input_genre = input("Digite um gênero de filme: ").strip().lower()

contador = 0

for i, g in enumerate(gr):   # filmes do gênero digitado pelo usuário + nome, ano e nota
    if input_genre in g.lower():
        print(f"Gênero: {g} | Nome: {mn[i]} | Ano: {yr[i]} | Nota: {mr[i]}")
        contador += 1
        
        if contador == 10:
            break
        

# RELATÓRIO

with open('relatorio.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write("Relatório de Filmes\n\n")
    relatorio.write("====================\n\n")
    relatorio.write(f"Descrição: Esse dataset contém dados de 10.000 filmes dos anos de 1915 a 2023\n\n")
    relatorio.write("====================\n\n")
    relatorio.write(f"Quantidade total de registros: {cont-1}\n")
    relatorio.write(f"Quantidade total de colunas: {len(leitor.fieldnames)}\n\n")
    relatorio.write("====================\n\n")
    relatorio.write("Estatísticas:\n")
    relatorio.write(f"Menor tempo de filme: {min(rt)} minutos\n")
    relatorio.write(f"Menor avaliação: {min(mr)}\n")
    relatorio.write(f"Maior tempo de filme: {max(rt)} minutos\n")
    relatorio.write(f"Maior avaliação: {max(mr)}\n")
    relatorio.write(f"Média do tempo de filme: {mediart:.2f} minutos\n")
    relatorio.write(f"Média da avaliação: {mediamr:.2f}\n\n")
    relatorio.write("====================\n\n")
    
    relatorio.write("Filtro: Filmes do ano 2000 com nota acima de 8.0:\n\n")
    
    contador = 0
    for i, y in enumerate(yr):
        if y == 2000 and mr[i] >= 8.0:
            relatorio.write(f"Ano: {y} | Nota: {mr[i]} | Nome: {mn[i]}\n")
            contador += 1
            if contador == 10:
                break
    
    relatorio.write("\nFiltro: Filmes com nota acima de 9.0:\n\n")
    contador = 0
    for i, m in enumerate(mr):
        if m >= 9.0:
            relatorio.write(f"Nota: {m} | Nome: {mn[i]}\n")
            contador += 1
            if contador == 10:
                break
    
    relatorio.write(f"\nFiltro: Filmes do gênero '{input_genre}':\n\n")
    contador = 0
    for i, g in enumerate(gr):
        if input_genre in g.lower():
            relatorio.write(f"Gênero: {g} | Nome: {mn[i]} | Ano: {yr[i]} | Nota: {mr[i]}\n")
            contador += 1
            if contador == 10:
                break
            
    relatorio.write("\n====================\n\n")
    relatorio.write("Conclusão: \n")
    relatorio.write("O dataset apresenta uma variedade de filmes com diferentes tempos de duração e avaliações. \n")
    relatorio.write("Observa-se que existem filmes com avaliações muito altas, indicando a presença de obras de destaque. \n")
    relatorio.write("Além disso, a análise dos filmes do ano 2000 revela que houve uma boa quantidade de filmes com notas acima de 8.0, sugerindo um ano de produções de qualidade. \n")
    relatorio.write("A diversidade de gêneros também é evidente, permitindo uma ampla gama de opções para os espectadores. \n")
    relatorio.write("Em resumo, o dataset oferece uma visão abrangente do panorama cinematográfico ao longo dos anos, destacando tanto os filmes mais curtos quanto os mais longos, bem como aqueles com as melhores avaliações.")
    