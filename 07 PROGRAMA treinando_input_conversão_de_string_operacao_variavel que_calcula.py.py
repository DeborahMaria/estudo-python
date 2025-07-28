#treinando_input_conversão_de_string_operacao.py

# na linha abaixo declaro uma variavel que tera como valor o input
#adiciono uma string para orientar ao usuario
nome_do_usuario = input("Qual é seu nome?")

#na linha abaixo mantenho a mesma estrategia da linha acima
idade_do_usuario = input("Quantos anos você tem?")

#na linha abaixo inicio a resolução do desafio que é converter 
#a string em int ,para que o dado seja processado como numero
#criando uma nova variavel e mudando o valor da mesma,apartir 
#de agora o valor da variavel sera calculavel
idade_do_usuario_int = int(idade_do_usuario)

#declaro variavel para caulcula idade_do_usuario_int
ano_de_ano_atual = 2025

#na linha abaixo uso a função print para imprimir os dados colocados
#pelo usuario ,junto a strings para passar uma impressão de interação
#faço o uso do f-string para fazer a junção dos dados do usuario de forma mais 
#simples sem precisar concatenar com o simbulo de +
print(f"Prazer em te conhecer! {nome_do_usuario} você tem só {idade_do_usuario_int} de idade!")
print(f"você nasceu em {ano_de_ano_atual - idade_do_usuario_int}")