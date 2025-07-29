#treinando_if_elif_else_usando_f-string.py

#declarado variavel com input para receber o valor do usario
temperatura = float (input("Digte a temperatura"))

#abaixo iniciado o bloco condicional com if para comerçar o desafio
if temperatura >=25:
    print(f"com {temperatura}° esta calor,pegue seus oculos de sol e use roupas leves")
    
#abaixo usarei alguns elif para que se o if não seja reconhecido como verdadeiro ele retorne uma das opções abaixo
#adicionei o uso do f-string para que a resposta fique mais ludica
elif temperatura >=20:
    print(f"com {temperatura}° o tempo esta agradavel, use roupas confortaveis")
    
elif temperatura >=15:
    print(f"com {temperatura}° esta um pouco frio, coloque um casaco")
    
else:
    print(f"com {temperatura}° esta frio, use um casaco reforçado")