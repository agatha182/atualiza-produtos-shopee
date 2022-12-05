import modulos.catavento as catavento
import modulos.shopee as shopee

def informacoes_basicas():
    print('Atualizando informações básicas.')
    print('\n')
    catavento.importa_estoque()
    shopee.importa_informacoes_basicas()

    
def informacoes_de_envio():
    print('Atualizando informações de envio.')
    print('\n')
    catavento.importa_estoque()

def informacoes_de_midia():
    print('Atualizando informações de mídia.')
    print('\n')
    catavento.importa_estoque()

def informacoes_de_vendas():
    print('Atualizando informações de vendas.')
    print('\n')
    catavento.importa_estoque()

def informacoes_fiscais():
    print('Atualizando informações fiscais.')
    print('\n')
    catavento.importa_estoque()

def informacoes_prazo_postagem():
    print('Atualizando informações sobre prazo de postagem.')
    print('\n')
    catavento.importa_estoque()




