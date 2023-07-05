import os
import csv
import json
import time

def clientes_json():
    time.sleep(5)

    for nome_Arquivo in os.listdir('C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes/'):#'/home/jeferson/aws-puppeteer/coreClientes/'
        if nome_Arquivo.endswith('.csv'):
            with open('C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes/' + nome_Arquivo) as f:
                print(f'Arquivo encontrado : {nome_Arquivo}')
                arquivo_json = 'clientes.json'
                dados = []
                reader = csv.reader(f, delimiter=';')
                headers = next(reader)
                for row in reader:
                    d = {}
                    for i, h in enumerate(headers):
                        # d[h] = row[i]
                        key = h.replace('\ufeffbirthCity', 'birthCity')
                        d[key] = row[i]
                    if d['situacao'] != 'Ativa':
                        dados.append(d)
                print('Buscando clientes Inativos')
                with open(arquivo_json, 'w') as file:
                    json.dump(dados, file, indent=4)
                    time.sleep(3)
                    print(f'Clientes filtrados e salvos em: {arquivo_json}')
    time.sleep(1.5)
    print('Exluindo arquivo em...')
    time.sleep(1.5)
    print('3')
    time.sleep(1.5)
    print('2')
    time.sleep(1.5)
    print('1')
    os.remove(f"C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes/{nome_Arquivo}")
    time.sleep(1.5)
    retorno = f'{nome_Arquivo} excluído!'
    return retorno
            
