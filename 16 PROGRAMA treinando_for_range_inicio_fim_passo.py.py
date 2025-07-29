#treinando_for_range_inicio_fim_passo

#a proposta é criar dois tipos de contagem e imprimir na tela , uma tera numeros pares de 0 a 10 e a segunda contagem tera de 1 a 9.
#primeiro dou inicio ao for,em seguida adiciono uma "variavel" que ira interagir com o a listagem, "in" fazendo a ponte
#e por fim adicionarei o range (inicio,fim,intervalo)
print ("Contagem de numeros pares")
for contador in range(0,11,2):
    print(f"par: {contador}")
    
print ("Contagem de numeros impares")
for contador in range(1,10,2):
    print(f"impar: {contador}")
    
#o primeiro for conta de 0 a 10 de 2 em 2 assim evidenciando os numeros pares
#o segundo for conta de 1 a 9 de 2 em 2 assim evidenciando os numeros impares