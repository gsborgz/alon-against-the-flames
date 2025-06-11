define playerName = ""

label part71:
    while not playerName:
            $ playerName = renpy.input("Como você se chama?", length=32).strip()

    $ player.name = playerName
