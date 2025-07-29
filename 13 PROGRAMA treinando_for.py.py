#treinando_for.py

#programa que apresenta uma lista de compras , usando a função 'for'.

#Declarado variavel que armazenara a lista, nela sera necessario o uso de colchetes, o uso da virgula para que haja separação 
#dos itens e as aspas , por se tratar de uma lista
compra_supermercado = ["arroz","feijão","batata","macarrão"]

#aqui é iniciado o uso da função for, compra é age como uma variavel temporaria, in faz a ponte entre a função , e por fim
#é chamada a variavel declarada no inicio do codigo, que fornecera os dados.
for compra in compra_supermercado:
    print (f"comprar: {compra}")


