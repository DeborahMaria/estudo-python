#treinando_len_for_range

#objetivo: criar uma lista de nomes, enumerada, valor total

#lista com os nomes 
lista_nome = ["maria","tereza","jose","pedro"]

#variavel com a quantidade de pessoas
quantidade_pessoas = len(lista_nome)

#cabeçalho
print ("__________lista de presença__________")

#quantidade de pessoas

print (f"nº total de pessoas {quantidade_pessoas}")

#for para listar os nomes, e range para enumerar

for sequencia_pessoas in range(len(lista_nome)):

	print(f"- {sequencia_pessoas}")
