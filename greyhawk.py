from random import randint

atuantes = []
destrezas_atuantes = {}

def main():
    anotaJogadores()
    anotaInimigos()

    while True:
        mostraAtuantes()

        print(
        """
        [a]dicionar atuante
        [r]emover atuante
        [g]erar iniciativa
        [f]inalizar o combate
        """)
        comando = input("Comando: ").lower()

        if comando == "a":
            tipo = input("[j]ogador ou [i]nimigo? R: ").lower()

            if tipo == "j":
                anotaJogadores()
            elif tipo == "i":
                anotaInimigos()
        elif comando == "r":
            apagaAtuantes()
        elif comando == "g":
            iniciativaGW()
        elif comando == "f":
            break


def anotaJogadores():
    """
    Atualiza a lista de jogadores
    """
    global atuantes, destrezas_atuantes

    i = 0
    while True:
        i += 1
        
        nome = input(f"Jogador {i}: ")
        if nome == "-":
            break

        atuantes.append(nome)
        destrezas_atuantes[nome] = int(input("Valor bruto de Destreza: "))

        print("\n")

    print("\n")

def anotaInimigos():
    """
    Atualiza a horda de inimigos
    """
    global atuantes

    while True:
        nome = input("Criatura: ")
        if nome == "-":
            break

        dex = int(input("Valor bruto de Destreza: "))

        quantidade = int(input("Quantidade: "))
        for i in range(quantidade):
            atuantes.append(f"{nome} {i + 1}")
            destrezas_atuantes[f"{nome} {i + 1}"] = dex

        print("\n")
    
    print("\n")

def mostraAtuantes():
    """
    Mostra a lista atual de atuantes na cena
    """
    global atuantes

    for i in range(len(atuantes)):
        print(f"{i + 1}: {atuantes[i]}", end=" | ")
    
    print("\n\n")

def apagaAtuantes():
    """
    Apaga itens de atuantes pelo índice
    """
    global atuantes, destrezas_atuantes

    removidos = [atuantes[int(n) - 1] for n in input("Números dos removidos: ").split()]

    for nome in removidos:
        destrezas_atuantes.pop(atuantes[atuantes.index(nome)])
        atuantes.remove(nome)


def iniciativaGW():
    """
    Recebe as ações de cada atuante e calcula a iniciativa usando o método de Greyhawk
    """
    global atuantes, destrezas_atuantes

    iniciativas_atuantes = {}
    dados = {"r": 4, "m": 6, "a": 8, "s": 10}

    # Recebe a lista de ações e calcula a iniciativa
    print("""
    Ações: 
        ataque [r]anged
        [m]ovimento / trocar equipamento / outro
        [a]taque melee
        [s]pell
    
    Situação especial:
        surpreendido[!]
    """)

    while True:
        indices_atuantes = input("Números dos atuantes: ")
        if indices_atuantes == "0":
            break

        conjunto_atuantes = [atuantes[int(indice_atuante) - 1] for indice_atuante in indices_atuantes.split()]
        acoes = input("Ações: ").lower()

        for atuante in conjunto_atuantes:
            iniciativa = 0
            for acao in acoes:
                if acao == "!":
                    iniciativa += 10
                elif acao in dados.keys():
                    iniciativa += randint(1, dados[acao])
            
            iniciativas_atuantes[atuante] = iniciativa
    
    # Organiza todas as iniciativas
    ordem_rodada = []
    for atuante, iniciativa in iniciativas_atuantes.items():
        i = 0
        atuante_inserido = False
        while i < len(ordem_rodada) and not atuante_inserido:
            if iniciativas_atuantes[ordem_rodada[i]] > iniciativa:
                ordem_rodada.insert(i, atuante)

                atuante_inserido = True
            elif iniciativas_atuantes[ordem_rodada[i]] == iniciativa:
                if destrezas_atuantes[ordem_rodada[i]] == destrezas_atuantes[atuante]:
                    if randint(0, 1):
                        ordem_rodada.insert(i, atuante)

                        atuante_inserido = True
                elif destrezas_atuantes[ordem_rodada[i]] < destrezas_atuantes[atuante]:
                    ordem_rodada.insert(i, atuante)

                    atuante_inserido = True

            i += 1
        
        if not atuante_inserido:
            ordem_rodada.append(atuante)

    # Mostra a ordem da rodada
    for nome in ordem_rodada:
        print(nome)
    

main()
