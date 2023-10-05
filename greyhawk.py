from random import randint

def main():
    jogadores = getPlayers()
    inimigos = getEnemies()

    while True:
        acoes = getActions(jogadores + inimigos)
        if len(acoes) == 0:
            break

        for iniciativa, atuantes in gwInitiative(acoes).items():
            print(f"{iniciativa}: {atuantes}")


def getPlayers():
    """
    Pega a lista de jogadores
    """
    l = []
    i = 1
    while True:
        name = input(f"jogador {i}: ")
        if name == "-":
            break

        l.append(name)
        i += 1

    return l

def getEnemies():
    """
    Pega a orda de inimigos
    """
    enemies = []
    while True:
        name = input(f"criatura: ")
        if name == "-":
            break

        num = int(input("quantidade: "))
        for i in range(num):
            enemies.append(f"{name} {i + 1}")

    return enemies


def getActions(actors):
    """
    Pega as ações de cada atuante
    """

    # Mostra a lista de atuantes
    for i in range(len(actors)):
        print(f"{i + 1}: {actors[i]}", end=" | ")
    
    # Mostra a lista de ações
    print("""
    [r]anged attack
    [m]ove/swap/other
    melee [a]ttack
    cast a [s]pell
    """)

    # Pega as ações
    acts = {}
    while True:
        actor = int(input("inimigo/jogador: ")) - 1
        if actor < 0:
            break

        acts[actors[actor]] = input("ações: ")
        print("\n")

    return acts

def gwInitiative(acts):
    """
    Calcula a iniciativa usando o método de Greyhawk.
    """

    # Inicia cada atuante com 0 de iniativa
    initiative = {}
    for actor in acts.keys():
        initiative[actor] = 0

    # Calcula o valor de cada ação de cada atuante
    for actor in acts.keys():
        dice = {"r": 4, "m": 6, "a": 8, "s": 10}

        for act in acts[actor]:
            initiative[actor] += randint(1, dice[act] + 1)

    # Organiza o turno em ordem de iniciativa
    turn = {}
    for i in range(1, 31):
        for actor, value in initiative.items():
            if value == i:
                try:
                    turn[str(i)] += f", {actor}"
                except:
                    turn[str(i)] = actor

    return turn
    

main()
