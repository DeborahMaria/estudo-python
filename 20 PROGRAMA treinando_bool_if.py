#treinando_bool_if_print

#Exercício 1: Acesso ao Evento
#Imagine que você está controlando a entrada em um evento. Para entrar, a pessoa precisa ser estudante E ter a idade mínima exigida de 16 anos.

#1 variavel com input para receber a idade do usuario, com string para instruir o usuario.
idade_usuario = int(input("Quantos anos você tem ?"))

#2 variavel com input para receber a resposta do usuario, com string para instruir o usuario.
estudante_usuario = (input("Você é estudante ?"))

#1 variavel com bool para verificar se é maior ou igual a 16 que é a idade necessaria para true
verificador_idade = idade_usuario >= 16

#2 variavel com bool para verificar se é estudante 
verificador_estudante_usuario = estudante_usuario == "sim"

if verificador_idade and verificador_estudante_usuario:
	print("Acesso permitido")

else:
	print("Acesso negado")


