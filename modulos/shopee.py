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
    importa_planilhas_informacoes_basicas()
    

    def importa_planilhas_informacoes_basicas():
        print('Realizando conexão com a planilha.')
        print('Isto pode levar alguns minutos, por favor aguarde...')
        planilha_info_basicas_df = pd.read_excel('planilhas_atualizar/shopee/Informacoes_basicas/1.xlsx')
        print('Conexão com a planilha realizada com sucesso.')
        print('Imprimindo dataframe obtido.')
        print('\n.')
        print(planilha_info_basicas_df)
        print('\n.')