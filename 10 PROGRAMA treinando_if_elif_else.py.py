#treinando_if_elif_else.py

#declarado variavel com input para receber o valor do usario
temperatura = float (input("Digte a temperatura"))

#abaixo iniciado o bloco condicional com if para comerçar o desafio
if temperatura >=25:
    print("Esta calor,pegue seus oculos de sol e use roupas leves")
    
#abaixo usarei alguns elif para que se o if não seja reconhecido como verdadeiro ele retorne uma das opções abaixo
elif temperatura >=20:
    print("O tempo esta agradavel, use roupas confortaveis")
    
elif temperatura >=15:
    print("Esta um pouco frio, coloque um casaco")
    
else:
    print("Esta frio, use um casaco reforçado")
