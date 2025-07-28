
#treinando_if_e_else.py

#vou declarar a abaixo uma variavel para ser a senha a ser verificada com asapas por ser uma string
senha = "python123"

#declarado uma nova variavel com input para ser comparada a senha criada
verificação = input()

#if para comparação de senha com verificação (os dois pontos vão no final da linha)
#o uso do == é para que tenha uma comparação
if senha == verificação:

     print("Acesso Liberado")


#else caso não seja a senha correta (os dois pontos são inseridos após a palavra else)

else:

    print("Senha incorreta, Acesso negado")

