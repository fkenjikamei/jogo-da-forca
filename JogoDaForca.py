import json
import random

'''
	Jogo da Forca em Python criado originalmente por Fernando Kenji Kamei
	Modificado e comentado por Ramon Rodrigues
'''
# carrando categoria do arquivo json
data = json.load(open('data.json'))

# jogador digita o nome
nome = str(input("Digite seu nome: "))
# titulo do jogo
print("\n*** Jogo da Forca em Python ***")
# mensagem de boas vidas
print("*** Bem vindo {name} ao jogo da forca em Python ***\n".format(name=nome))
# imprime a lista de categorias contida no arquivo JSON
print("\n*** Escolha uma categoria abaixo ***")
for item in data:
	print('*',item)
# pergunta a categoria
categoria = input("Digite a categoria: ")
# palavra secreta a ser descobrida
palavra_secreta = data[categoria][random.randrange(0, len(data[categoria]))]
# aqui fica armazenado as letras já descobertas
letras_descobertas = []

# se a palavra ainda não foram descobertas adiciona um "-"
for i in range(0, len(palavra_secreta)):
	letras_descobertas.append("-")

# false para fazer loop até descubrir
acertou = False

# se acertou é false pede uma letra
while acertou == False:
	letra  = str(input("Digite uma letra: "))

	# verifica se a letra está correta e substitui o "-" pela letra
	for i in range(0, len(palavra_secreta)):
		if letra == palavra_secreta[i]:
			letras_descobertas[i] = letra
		print(letras_descobertas[i])

	# descubriu uma letra deixa "acertou" verdadeiro
	acertou = True

	# verifica se ainda existe "-" se sim  retorna ao loop até descubrir
	for x in range(0, len(letras_descobertas)):
		if letras_descobertas[x] == "-":
			acertou = False

# mensagem de acerto de todas as letras
print("\n*** Parabens {name}, você descubriu a palavra ***\n".format(name=nome))
