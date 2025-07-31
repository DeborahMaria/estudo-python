#O Desafio:
#Crie um programa que:

#Peça ao usuário seu nome usando input().

#Crie uma lista com pelo menos 5 nomes de produtos (strings).

#Crie uma segunda lista com os preços correspondentes a cada produto da primeira lista (números, podem ser float ou int).

#Use um for loop com range() para percorrer as listas. A cada item, exiba o produto e seu preço de forma formatada (usando f-string). Ex: "1. Camiseta - R$ 59.90".

#Peça ao usuário para escolher um número de produto para aplicar um desconto. Use input() e converta para int().

#Use uma estrutura if/elif/else para verificar o número que o usuário digitou:

#Se o número for válido (dentro do range dos produtos):

#Calcule o preço com 10% de desconto para o produto escolhido.

#Exiba uma mensagem de agradecimento usando o nome do usuário e informando o nome do produto escolhido e o novo preço com desconto.

#Se o número for inválido (fora do range dos produtos):

#Exiba uma mensagem informando que a escolha foi inválida.

-------

# desafio_com_funcao

#criar um programa exibir produtos, calcular desconto, validar escolha do cliente.

#declaro variavel que armazenara a lista de produtos.
produtos = ["camiseta","calça","meia","touca","sapato","luva"]

preços = [50,100,10,10,15,200,5]

#lista feita, agora com o for 
print ("----------VESTUARIO-----------")
for listage_produtos in produtos:



