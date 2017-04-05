#coding: utf-8
import json
import random

letras_descobertas = [] # aqui fica armazenado as letras já descobertas, redundante, pois o nome da variável é auto explicativo
quantidadeLetrasDescobertas = 0
acertou = False # false para fazer loop até descubrir

data = json.load(open('data.json')) # carrega dados do arquivo json

nome = str(input("Digite seu nome: "))

print("\n*** Jogo da Forca em Python ***") # titulo do jogo
print("*** Bem vindo {nome} ao jogo da forca em Python ***\n".format(nome=nome)) # mensagem de boas vidas
print("\n*** Escolha uma categoria abaixo ***") # imprime a lista de categorias contida no arquivo JSON

for item in data: 
	print('*',item) # pergunta a categoria

categoria = str(input("Digite a categoria: ")).lower()
palavra_secreta = data[categoria][random.randrange(0, len(data[categoria]))] # sorteia a palavra secreta a ser descobrerta

#print(palavra_secreta) #inserido para facilitar os testes --------------SERÁ DELETADO DEPOIS-----------

for i in range(0, len(palavra_secreta)): # se a palavra ainda não foram descobertas adiciona um "-"
	letras_descobertas.append("-")

while (acertou == False): # Enquanto acertou for igual a false e a quantidade de erros for menor que o limite, o jogo continua
	if(quantidadeLetrasDescobertas > 0): #Se tudo for zero, não será mostrado
		print("Acertos", quantidadeLetrasDescobertas)
	
	letra  = str(input("Digite uma letra: ")).lower() #Será convertido para minúsculo qualquer caractere

	for interator in range(0, len(palavra_secreta)): # verifica se a letra está correta e substitui o "-" pela letra
		if (letra == palavra_secreta[interator]):
			
			quantidadeLetrasDescobertas += 1
			letras_descobertas[interator] = letra.upper()
		print(letras_descobertas[interator])
	
	if (quantidadeLetrasDescobertas == len(palavra_secreta)):
		print("Fim do jogo, você descobriu a palavra secreta,",palavra_secreta)
		acertou = True

	for x in range(0, len(letras_descobertas)): # verifica se ainda existe "-" se sim  retorna ao loop até descubrir
		if (letras_descobertas[x] == "-"):
			acertou = False