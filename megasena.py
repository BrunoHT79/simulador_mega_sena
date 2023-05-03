import random

def joga():

    print("**********************************")
    print("* Simulador de Jogo da Mega-Sena *")
    print("**********************************")

    numeros_sorteados = random.sample(range(1, 61), 6)
    numeros_sorteados.sort()
    indice = 0
    numeros_escolhidos = []

    while indice < 6:
        numeros = int(input("Qual {}o. número você gostaria de apostar: ".format(indice+1)))
        numeros_escolhidos.insert(indice,numeros)
        indice = indice + 1

    numeros_escolhidos.sort()
    print(numeros_sorteados)
    print(numeros_escolhidos)

if __name__ == "__main__":
    joga()