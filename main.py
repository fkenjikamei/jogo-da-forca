import random, json, os
from imprimir import Imprimir

letrasUsadas = "" #serve para armazenar as letras que já foram digitadas
caracterespermitidos = "abcdefghijklmnopqrstuvwxyz" #limita os caracteres usados no código
palavraEscolhida = ""
letrasDescobertas = []
limiteErros = 6
acertoLetras = 0
erroLetras = 0

desenhoTela = Imprimir()
os.system('cls' if os.name == 'nt' else 'clear') #Vai limpar tela, tanto no windows ou linux
data = json.load(open('data.json')) # carrega dados do arquivo json
nome = input("Digite seu nome: ")
print("\n*** Jogo da Forca em Python ***") # titulo do jogo
print("*** Bem vindo ao jogo {} ***\n".format(nome)) # mensagem de boas vidas
print("\n*** Escolha uma categoria abaixo ***") # imprime a lista de categorias contida no arquivo JSON

for item in data:
	print('*',item) # pergunta a categoria

verificaCategoria = False
while verificaCategoria == False:
    categoria = input("Digite a categoria: ").lower()
    if(categoria == "frutas" or categoria == "nomes"):
        verificaCategoria = True
    else:
        print("Nome da categoria inválido")

palavraEscolhida = data[categoria][random.randrange(0, len(data[categoria]))] # sorteia a palavra secreta a ser descobrerta
os.system('cls' if os.name == 'nt' else 'clear') #Vai limpar tela, tanto no windows ou linux
desenhoTela.desenharNaTela(0)

for i in range(0, len(palavraEscolhida)): # se a palavra ainda não foram descobertas adiciona um "-"
        letrasDescobertas.append("-")

print(letrasDescobertas, "\nA palavra contém,", len(palavraEscolhida),"letras")

def entradaTeclado():
    verificaLetra = False
    verificaRepetida = False
    verificarNaPalavraSecreta = False
    reserva = "" #Criada apenas para exibir em linha
    global letrasUsadas, erroLetras, acertoLetras, letrasDescobertas

    entradaLetra = input("Digite a letra: ").lower()
    if(len(entradaLetra) == 1):

        for i in range(0, len(caracterespermitidos)): #Será verificado se a letra é válida, dentro do escopo inicial de letras permitidas
            if (entradaLetra == caracterespermitidos[i]):
                print("Caractere encontrado")
                verificaLetra = True

    if verificaLetra == True: #Agora é verificado se a letra já foi digitada pelo usuário antes
        for i in range(0, len(letrasUsadas)):
            if entradaLetra == letrasUsadas[i]:
                print("Letra já usada, digite novamente") #Evitar de registrar caractere repetido
                verificaRepetida = True
                entradaTeclado()

        if verificaRepetida == False: #Se cair neste bloco, é por não ser repetida
            letrasUsadas += entradaLetra

            for i in range(0, len(palavraEscolhida)):
                if(entradaLetra == palavraEscolhida[i]): #Verifica se a letra digitada existe na palavra escolhida
                    verificarNaPalavraSecreta = True
                    acertoLetras += 1
                    letrasDescobertas[i] = entradaLetra #Vai preencher visual as letras

            if verificarNaPalavraSecreta == True:
                print("Existe a letra", entradaLetra,"\nPróxima letra")

            else:
                print("Não existe a letra {letra} na palavra secreta".format(letra=entradaLetra))
                erroLetras += 1
        else:
            entradaTeclado()

    if verificaLetra == False:
        print("Caractere inválido ")
        entradaTeclado()
    os.system('cls' if os.name == 'nt' else 'clear') #Vai limpar tela, tanto no windows ou linux
    desenhoTela.desenharNaTela(erroLetras)
    print("Letras já digita", letrasUsadas)
    for i in range(0, len(palavraEscolhida)): #Vai passar dentro da palavra secreta para desenhar na tela
        reserva += letrasDescobertas[i]
    print("\n", reserva)

while erroLetras < limiteErros and acertoLetras < len(palavraEscolhida): #Definição do que pode dar game over e vitória
    if (erroLetras == 5):
        print("Última tentativa, próximo erro, perde o jogo. ")
    entradaTeclado()

if acertoLetras >= len(palavraEscolhida) and acertoLetras > 0: #Resposta para a condição de vitória
    print("Parabéns", nome, "você descobriu a palavra secreta", palavraEscolhida)

if erroLetras >= limiteErros: #Resposta para a condição de game over
    print(nome, "infelizmente você atingiu o limite de erros, a palavra secreta é", palavraEscolhida)