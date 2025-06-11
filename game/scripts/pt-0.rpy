define attrs = [
    ("Força", "playerSTR"),
    ("Constituição", "playerCON"),
    ("Poder", "playerPOW"),
    ("Destreza", "playerDEX"),
    ("Aparência", "playerAPP"),
    ("Tamanho", "playerSIZ"),
    ("Inteligência", "playerINT"),
    ("Educação", "playerEDU"),
]

label intro:

    "Você tem oito atributos: Força, Constituição, Poder, Destreza, Aparência, Tamanho, Inteligência e Educação."
    "Você pode distribuir os seguintes valores entre eles: 40, 50, 50, 50, 60, 60, 70 e 80."

    $ valoresDisponiveis = ["40", "50", "50", "50", "60", "60", "70", "80"]
    $ attrsDict = {}

    python:
        for name, var in attrs:
            valorSetado = False
            while not valorSetado:
                valor = renpy.input("Valores disponíveis: " + ", ".join(valoresDisponiveis) + f"\nDefina o valor de {name}:", allow="0123456789").strip()
                if valor in valoresDisponiveis:
                    attrsDict[var] = valor
                    valoresDisponiveis.remove(valor)
                    valorSetado = True
                else:
                    renpy.say(None, f"O valor de {name} deve ser um dos seguintes: {', '.join(valoresDisponiveis)}.")

        player.setAttributes(attrsDict)

    "Agora você precisará jogar três dados de seis lados (3d6) para determinar seus pontos de sorte."

    $ valuesRolled = []
    menu:
        "Jogar D6":
            $ value = Dice.rollD6()
            $ player.luckPoints += value
            $ valuesRolled.append(value)
            $ renpy.say(None, f"Você rolou: {', '.join(map(str, valuesRolled))}")
            


    menu:
        "Jogar D6":
            $ value = Dice.rollD6()
            $ player.luckPoints += value
            $ valuesRolled.append(value)
            $ renpy.say(None, f"Você rolou: {', '.join(map(str, valuesRolled))}")

    menu:
        "Jogar D6":
            $ value = Dice.rollD6()
            $ player.luckPoints += value
            $ valuesRolled.append(value)
            $ renpy.say(None, f"Você rolou: {', '.join(map(str, valuesRolled))}")

    $ player.luckPoints *= 5

    "A soma dos resultados será multiplicada por 5, sendo assim, você terá inicialmente [player.luckPoints] pontos de sorte."
    "Esta é uma aventura para o RPG Chamado de Cthulhu. É uma história de horror ambienta da na década de 1920 em que você é o personagem principal e suas escolhas determinam o resultado da trama."
    "Acomode-se em uma cadeira confortável perto do fogo da lareira e então embarque nesta aventura."
    "... Pensando bem, não se sente muito perto do fogo."

    call part1

    return
