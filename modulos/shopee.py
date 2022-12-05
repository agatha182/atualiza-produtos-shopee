import pandas as pd
import os

def importa_informacoes_basicas():
    print('Realizando importação das planilhas da shopee para atualização.')
    contagem_inicial = 0
    dir = "planilhas_atualizar/shopee/Informacoes_basicas"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            contagem_inicial += 1
    print(f'Foram identificadas '+str(contagem_inicial)+' planilhas a serem atualizadas.')
    print('Realizando conexão com as planilhas.')
    print('Isto pode levar alguns minutos, por favor aguarde...')
    print('Conexão com a planilha realizada com sucesso.')