import pandas as pd

def importa_estoque():
    print('Qual fonte você quer usar para importar o estoque da catavento?')
    print('\n')
    print('[1] Importar estoque por meio da planilha.')
    print('[2] Importar estoque por meio da API.')
    print('\n')
    escolha = int(input('Escolha sua opção: '))

    if (escolha == 1):
        importa_estoque_planilha()
    if (escolha == 2):
        print('Infelizmente a conexão com a API ainda não está disponível.')


def importa_estoque_planilha():
    print('A importação será realizada por meio da planilha excel.')
    print('Realizando conexão com a planilha.')
    print('Isto pode levar alguns minutos, por favor aguarde...')
    estoque_df = pd.read_excel('estoque/estoquecatavento.xlsx')
    print('Conexão com a planilha realizada com sucesso.')
    print('Imprimindo dataframe obtido.')
    print('\n.')
    print(estoque_df)
    print('\n.')



