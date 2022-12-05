import pandas as pd
import modulos.atualiza as atualiza

print('\n')
print('\n')
print('Escolha umas das opções abaixo:')
print('\n')

print('[1] Atualizar informações básicas.')
print('[2] Atualizar informações de envio.')
print('[3] Atualizar informações de mídia.')
print('[4] Atualizar informações de vendas.')
print('[5] Atualizar informações fiscais.')
print('[6] Atualizar informações sobre prazo de postagem.')
print('\n')

menu = int(input('Escolha sua opção: '))
print('\n')

if (menu == 1):
    atualiza.informacoes_basicas()

if (menu == 2):
    atualiza.informacoes_de_envio()

if (menu == 3):
    atualiza.informacoes_de_midia()

if (menu == 4):
    atualiza.informacoes_de_vendas()

if (menu == 5):
    atualiza.informacoes_fiscais()

if (menu == 6):
    atualiza.informacoes_prazo_postagem()