label part71:
    "Você retoma sua jornada. O motorista faz as curvas com mais cautela do que antes."
    "Ele olha por cima do ombro, em sua direção, algumas vezes."

    $ busdriver.say("Desculpe por aquilo, aquele cara era mais burro que um porco. Eu sou Silas.")
    $ busdriver.updateCharacter("Silas", None, None)
    $ busdriver.say("Como você se chama?")
    $ busdriver.hide()

    python:
        playerName = ""

        while not playerName:
            playerName = renpy.input("Digite o seu nome:", length=32).strip()

        player.name = playerName

    "O acidente foi no mínimo tanto culpa de Silas quanto do fazendeiro."
    "Mas não parece inteligente antagonizar o homem enquanto ele está dirigindo apenas para você no meio do nada."
    "O ônibus toma uma estrada mais estreita, que serpenteia subindo por colinas tomadas por flores tas. Silas fica conversador."

    $ busdriver.say("Indo para Arkham, né? Não posso dizer que já ouvi falar do lugar. Fui pra Boston uma vez. Não gostei.")
    $ busdriver.say("Muita agitação. Você tem família lá? Alguém especial te esperando?")
    $ busdriver.disable()

    "A tarde está acabando. Você não vê nenhum mal em falar para Silas sobre sua nova vida."

    $ busdriver.say("Um emprego é? E trabalha com o quê?")
    $ busdriver.hide()

    if player.occupation == PlayerOccupation.ANTIQUARIAN:
        call part102
    elif player.occupation == PlayerOccupation.DOCTOR:
        call part226
    elif player.occupation == PlayerOccupation.JOURNALIST:
        call part239
    elif player.occupation == PlayerOccupation.INVESTIGATOR:
        call part249
    elif player.occupation == PlayerOccupation.PROFESSOR:
        call part265
