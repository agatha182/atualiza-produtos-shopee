# Atualizar informações de produtos cadastrados na Shopee
Este é o meu fork da aplicação do tiagolisboanovais, cujo README original segue abaixo:

Esta é uma aplicação em python que visa facilitar o processo de atualização das informações de produtos que estejam cadastrados na Shopee. A forma inicial que iremos usar para atualizar estas informações, será através das planilhas de edição em massa fornecidos pela própria plataforma. Futuramente, caso consigamos acesso a API da plataforma, estabeleceremos uma comunicação direta, de forma que não será mais necessário fazer isto por meio de planilhas.

A Shopee trabalha com 6 tipos de planilhas para atualização de estoque, cada planilha é responsável pela edição de certos informações dos produtos, que são elas:



1. Informações básicas
2. Informações de envio
3. Informações de mídia
4. Informações de vendas
5. Informações fiscais
6. Informações sobre prazo de postagem



#### Quais campos são editados em cada tipo de planilha?

Abaixo uma relação de quais campos são editados em cada tipo de planilha. É importante ressaltar que existe um número 1900 linhas de limite para cada planilha, ou seja, se houver mais que 1900 produtos a serem realizados, serão geradas quantas planilhas forem necessárias para que todos os produtos sejam atualizados.



##### 1. Informações básicas

Na planilha de informações básicas existem 4 colunas, sendo que destas, somente 3 colunas são editáveis, estas estão destacadas em negrito na relação abaixo. 

1. ID do Produto
2. **SKU de referência,**

3. **Nome do Produto**

4. **Descrição do Produto**

O campo ID do produto é fornecido automaticamente pela plataforma, este é utilizado para referenciar os produtos, quando o upload da planilha for realizado.



**2. Informações de Envio**

Na planilha de informações de envio existem 9 colunas, sendo que destas, somente 4 colunas são editáveis, estas estão destacadas em negrito na relação abaixo. 

1. ID do Produto 
2. SKU de referência 
3. Nome do Produto 
4. **Peso do produto**
5. **Comprimento **
6. **Largura** 
7. **Altura**
8. Taxa de permuta 
9. Taxa de frete

O campo ID do produto é fornecido automaticamente pela plataforma, este é utilizado para referenciar os produtos, quando o upload da planilha for realizado. Os campos SKU de referência e Nome do produto estão na planilha para facilitar a identificação de qual produto está sendo alterado.



**3. Informações de mídia**

Na planilha de informações de envio existem 9 colunas, sendo que destas, somente 4 colunas são editáveis, estas estão destacadas em negrito na relação abaixo. 









