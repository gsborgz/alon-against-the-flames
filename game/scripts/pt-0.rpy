label intro:
    "Esta é uma aventura para o RPG Chamado de Cthulhu. É uma história de horror ambientada na década de 1920 em que você é o personagem principal e suas escolhas determinam o resultado da trama."
    "Acomode-se em uma cadeira confortável perto do fogo da lareira e então embarque nesta aventura."
    "... Pensando bem, não se sente muito perto do fogo."
    # "Antes de começarmos, como isso se trata de uma aventura de RPG, você precisará criar sua ficha de ersonagem."
    # "Não precisa se preocupar com todos os detalhes, pois sua ficha irá se formar ao longo da história."
    # "Mas para começarmos, será necessário que você defina alguns atributos básicos do seu personagem."
    # "Você possui oito atributos: Força, Constituição, Poder, Destreza, Aparência, Tamanho, Inteligência e Educação."
    # "Você pode distribuir os seguintes valores entre eles: 40, 50, 50, 50, 60, 60, 70 e 80."
    # "Seus pontos de vida serão determinados pela soma de sua Constituição e seu Tamanho, dividida por 10, arredondada para baixo."
    # "Já seus pontos de magia serão iguais a um quinto do seu Poder e seus pontos de sanidade serão iguais ao seu Poder."
    # "Não se preocupe em fazer esses cálculos agora, eles serão feitos automaticamente quando você definir seus atributos a seguir."
    # "Agora vamos distribuir os valores entre os atributos."

    call attributesDefinition

label attributesDefinition:
    # Remover criação de ficha do 0 por enquanto
    # python:
        # attrs = [
        #     ("Força", "playerSTR"),
        #     ("Constituição", "playerCON"),
        #     ("Poder", "playerPOW"),
        #     ("Destreza", "playerDEX"),
        #     ("Aparência", "playerAPP"),
        #     ("Tamanho", "playerSIZ"),
        #     ("Inteligência", "playerINT"),
        #     ("Educação", "playerEDU"),
        # ]
        # player.reset()
        # valoresDisponiveis = ["40", "50", "50", "50", "60", "60", "70", "80"]
        # attrsDict = {}

        # for name, var in attrs:
        #     valorSetado = False
        #     while not valorSetado:
        #         valor = renpy.input("Valores disponíveis: " + ", ".join(valoresDisponiveis) + f"\nDefina o valor de {name}:", allow="0123456789").strip()
        #         if valor in valoresDisponiveis:
        #             attrsDict[var] = valor
        #             valoresDisponiveis.remove(valor)
        #             valorSetado = True
        #         else:
        #             renpy.say(None, f"O valor de {name} deve ser um dos seguintes: {', '.join(valoresDisponiveis)}.")

        # player.setAttributes(attrsDict)

        # renpy.say(None, "Antes de terminarmos você precisará jogar três dados de seis lados (3d6).")
        # renpy.say(None, "Os resultados das três rolagens serão somados e multiplicados por 5 para determinar seus pontos de sorte iniciais.")

        # result = dice.rollD6(3)
        # player.luckPoints = sum(result) * 5
        # renpy.say(None, f"Resultado: {', '.join(map(str, result))}")

    menu:
        "Escolha um arquétipo de personagem:"

        "Antiquário":
            $ player = ArchetypeBuilder.buildAntiquarian()

        "Médico":
            $ player = ArchetypeBuilder.buildDoctor()

        "Jornalista":
            $ player = ArchetypeBuilder.buildJournalist()

        "Investigador":
            $ player = ArchetypeBuilder.buildInvestigator()

        "Professor":
            $ player = ArchetypeBuilder.buildProfessor()

    "Você escolheu o arquétipo {color=#0000ffff}[player.occupation.name]{/color}."
    "Antes de terminarmos você precisará jogar três dados de seis lados (3d6)."
    "Os resultados das três rolagens serão somados e multiplicados por 5 para determinar seus pontos de sorte iniciais."

    $ result = dice.rollD6(3)
    $ player.stats.luckPoints = sum(result) * 5
    $ renpy.say(None, f"Resultado: {', '.join(map(str, result))}")

    "Seu personagem ficou assim:\nForça: {color=#0000ffff}[player.attributes.str]{/color} Constituição: {color=#0000ffff}[player.attributes.con]{/color}\nPoder: {color=#0000ffff}[player.attributes.pow]{/color} Destreza: {color=#0000ffff}[player.attributes.dex]{/color}\nContinuar..."
    "Aparência: {color=#0000ffff}[player.attributes.app]{/color} Tamanho: {color=#0000ffff}[player.attributes.siz]{/color}\nInteligência: {color=#0000ffff}[player.attributes.int]{/color} Educação: {color=#0000ffff}[player.attributes.edu]{/color}\nContinuar..."
    "Pontos de vida: {color=#0000ffff}[player.stats.healthPoints]{/color} Pontos de sanidade: {color=#0000ffff}[player.stats.sanityPoints]{/color}\nPontos de magia: {color=#0000ffff}[player.stats.magicPoints]{/color} Pontos de sorte: {color=#0000ffff}[player.stats.luckPoints]{/color}"

    menu:
        "Você está satisfeito com esse personagem?"

        "Sim":
            jump part1

        "Não, quero criar outro.":
            jump attributesDefinition
