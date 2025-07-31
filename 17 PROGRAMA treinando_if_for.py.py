# treinando_if_for

#o desafio é criar uma lista de itens, e imprimir na tela uma frase especifica para cada item

#como itens da lista, foi adicionado algumas funções ,porem por possuirem aspas seram tratadas com string(texto)
lista_funcoes = ["print","input","if","for","range"]

#abaixo sera iniciado o uso do for e em sequencia o uso do if.
#para que o if funcione preciso colocar o for, para usar a "variavel temporaria" nas funções de comparação
#lembrando que tudo precisa estar indentado (com espaço) para que o seja possivel a interpretação mais adequada e na ordem correta

#adicionado um print incial para ser o cabeçalho 

print("****** Estudando funções ******")

#para usar o for, primeiro é criado uma "variavel temporaria" ,in de ponte e por fim a variavel que armazena a lista (lista_funcoes)
for funcao_da_vez in lista_funcoes:

    if funcao_da_vez =="print":
        print(f"{funcao_da_vez} essa função é usada para imprimir na tela")
    
    elif funcao_da_vez =="input":
        print(f"{funcao_da_vez} essa função é usada para que o usuario escreva algo")
    
    elif funcao_da_vez =="if":
        print(f"{funcao_da_vez} essa função é usada para condicionais, ela tem o eli e o else como complemento")
    
    elif funcao_da_vez =="for":
        print(f"{funcao_da_vez} essa função é usada para criar loop controlado")
    
    else:
        print(f"{funcao_da_vez} essa função é usada para gerar um contador de posição")
        
#após o for, deixei o if indentado, dentro de cada bloco com if e elif é referenciado duas vezes uma para comparação
#e uma segunda vez para que ele imprima 
    
