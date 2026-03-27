import csv



with open('data.csv', 'r',
          encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    cont = 0
    
    for linha in leitor:
        print(linha['Run Time in minutes'])
        if cont == 5:
            break

        print(linha)
        cont += 1