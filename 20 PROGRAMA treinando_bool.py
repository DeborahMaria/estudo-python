
# maior ou menor que 10

#declarado variavel com int para converter o input de str para int, com uma string para instruir o usuario 
valor = int(input("Digite um nuemro:"))

#abaixo uma variavel com valor bool , bool ou é true (verdadeiro) ou false (falso)
#se o numero inserido no input for maior que 10, resultara em true, caso contrario false
verificador = valor > 10

#abaixo há um bloco condicional onde se a variavel for verdadeira ou falsa apresentara uma mensagem na tela
if verificador:
    print ("maior que 10")
    
else:
    print ("menor que 10")