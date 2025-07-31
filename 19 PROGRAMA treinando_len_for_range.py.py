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
======================================================================
---

Essa é uma pergunta fundamental! É nesse ponto que todos os conceitos se conectam, e entender essa linha é um grande passo.

Vamos desmembrar a linha `print(f"- {sequencia_pessoas}. {lista_nome[sequencia_pessoas]}" )` em três partes:

### 1. Por que as chaves `{}`?

As **chaves `{}`** são usadas porque você está dentro de uma **f-string**. Lembra que a f-string é a maneira mais moderna de misturar texto com o valor das suas variáveis?

Tudo o que está **dentro das chaves `{}`** é código Python que será executado e o resultado será inserido no texto.

* `{sequencia_pessoas}`: Coloca o valor da variável `sequencia_pessoas` (o índice: 0, 1, 2...).
* `{lista_nome[sequencia_pessoas]}`: Coloca o resultado de `lista_nome[sequencia_pessoas]`.

---

### 2. Por que `lista_nome` e `[]` (colchetes)?

A `lista_nome` é a sua **caixinha grande** que guarda todos os nomes.

Os **colchetes `[]`** servem para **acessar um item específico** dentro dessa lista. Pense neles como o "seletor" que você usa para pegar apenas um nome.

* `lista_nome[0]` pega o primeiro nome ("maria").
* `lista_nome[1]` pega o segundo nome ("tereza").
* E assim por diante.

---

### 3. Por que `sequencia_pessoas` está dentro dos colchetes `[]`?

Essa é a parte mais inteligente e o motivo de usarmos `range(len())`.

A variável `sequencia_pessoas` está dentro do seu `for` loop:
`for sequencia_pessoas in range(len(lista_nome)):`

Isso significa que, a cada repetição do loop, a variável `sequencia_pessoas` vai assumir um valor diferente, que é o **índice** do item atual:
* **1ª vez:** `sequencia_pessoas` é `0`.
* **2ª vez:** `sequencia_pessoas` é `1`.
* **3ª vez:** `sequencia_pessoas` é `2`.

Então, quando você escreve `lista_nome[sequencia_pessoas]`, o Python faz isso em cada repetição:
* **1ª vez:** Pega `lista_nome[0]`, que é "maria".
* **2ª vez:** Pega `lista_nome[1]`, que é "tereza".
* **3ª vez:** Pega `lista_nome[2]`, que é "jose".

Em resumo: o `for` loop te dá o **índice**, e você usa esse **índice** para pegar o **item correspondente** na lista.

---

Ficou mais claro agora como a **f-string** usa as **chaves `{}`** para mostrar a **variável do loop** e o **item da lista** que é selecionado pelo **índice** do loop?