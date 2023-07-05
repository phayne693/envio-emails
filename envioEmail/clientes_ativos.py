import os
import csv
import json
import time
import pandas as pd

def clientes_ativos_json():
    time.sleep(5)
    for nome_Arquivo in os.listdir('C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes'):#'/home/jeferson/aws-puppeteer/coreClientes/'
        if nome_Arquivo.endswith('.csv'):
            with open('C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes/' + nome_Arquivo) as f:
                print(f'Arquivo encontrado : {nome_Arquivo}')
                arquivo_json = 'clientes_ativos.json'
                dados = []
                reader = csv.reader(f, delimiter=';')
                headers = next(reader)
                for row in reader:
                    d = {}
                    for i, h in enumerate(headers):
                        # d[h] = row[i]
                        key = h.replace('\ufeffbirthCity', 'birthCity')
                        d[key] = row[i]
                    if d['situacao'] == 'Ativa':
                        dados.append(d)
                with open(arquivo_json, 'w') as file:
                    json.dump(dados, file, indent=4)
                    time.sleep(3)
                    print(f'Clientes filtrados e salvos em: {arquivo_json}')
                #le o arquivo json e filtra os dados necessarios
                with open('clientes_ativos.json', 'r') as file:
                    dados = json.load(file)
                    clientes_ativos = []
                    #passa por todos os clientes salvos e pega os dados necessarios, nome, nascimento e cpf
                    for cliente in dados:
                        #para puxar os dados de um json declara a variavel, utilza o primeiro ponteiro do for(cliente) depois a chave:nome = cliente['name']
                        nome = cliente['name']
                        data_nascimento = cliente['birthDate']
                        cpf = cliente['taxId']
                        clientes_ativos.append(
                            {'nome': nome,
                             'data_nascimento': data_nascimento, 
                             'cpf': cpf
                             })
                        print(clientes_ativos)
                    # #escreve os dados em csv
                    # with open('clientes_ativos.csv', 'w', newline='') as file:
                    #     writer = csv.DictWriter(file, fieldnames=['nome', 'data_nascimento', 'cpf'])
                    #     writer.writeheader()
                    #     writer.writerows(clientes_ativos)
                    df = pd.DataFrame(clientes_ativos)
                    df.to_csv('clientes_ativos.csv', sep=';', index=False)
    time.sleep(1.5)
    retorno = "Arquivo clientes_ativos.csv, criado com sucesso!"
    return retorno
