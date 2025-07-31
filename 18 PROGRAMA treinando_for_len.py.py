# treinando_for_len

#contagem de itens de uma lista sem predefinir a quantidade usando a função len()

#declaro variavel com lista de itens 

material = ["caneta","boracha","lapis","apontador","regua"]

#com len identificaremos a quantidade de itens,porem é necessario que declare uma variavel para armazenar a lista

lista_de_material = len(material)

#cabeçalho
print("----------INVENTARIO----------")

print(f"na mochila tem:{lista_de_material} itens")

for itens in material:

	print(f"- {itens}")
    
    
    
    

