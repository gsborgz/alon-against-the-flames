transform enabled:
    matrixcolor BrightnessMatrix(0)

transform disabled:
    matrixcolor BrightnessMatrix(-0.5)

init python:
    import random

    class Dice:
        @staticmethod
        def rollD100():
            return random.randint(1, 100)

        @staticmethod
        def rollD6():
            return random.randint(1, 6)

    class Player:
        def __init__(self):
            # Strength (STR), Constitution (CON), Power (POW), Dexterity (DEX), Appearance (APP), Size (SIZ), Intelligence (INT), and Education (EDU).
            # Força (FOR), Con stituição (CON), Poder (POD), Destreza (DES), Aparência (APA), Tamanho (TAM), Inteligência (INT) e Educação (EDU).
            self.name = ""
            self.healthPoints = 0
            self.sanityPoints = 0
            self.magicPoints = 0
            self.luckPoints = 0
            self.attributes = {
                "STR": 0,
                "CON": 0,
                "POW": 0,
                "DEX": 0,
                "APP": 0,
                "SIZ": 0,
                "INT": 0,
                "EDU": 0
            }

        def takeHealthDamage(self, damage):
            self.healthPoints -= damage

        def restoreHealth(self, amount):
            self.healthPoints += amount

        def takeSanityDamage(self, amount):
            self.sanityPoints -= amount

        def restoreSanity(self, amount):
            self.sanityPoints += amount

        def setAttributes(self, attrs):
            player.attributes.STR = int(attrs["playerSTR"])
            player.attributes.CON = int(attrs["playerCON"])
            player.attributes.POW = int(attrs["playerPOW"])
            player.attributes.DEX = int(attrs["playerDEX"])
            player.attributes.APP = int(attrs["playerAPP"])
            player.attributes.SIZ = int(attrs["playerSIZ"])
            player.attributes.INT = int(attrs["playerINT"])
            player.attributes.EDU = int(attrs["playerEDU"])
            player.healthPoints = (player.attributes.SIZ + player.attributes.CON) // 10
            player.sanityPoints = player.attributes.POW
            player.magicPoints = player.attributes.POW // 5

        def setAttribute(self, attr, value):
            self.attributes[attr] = value

        def testAttribute(self, attr, roll, difficulty="normal"):
            values = {
                "STR": self.attributes.STR,
                "CON": self.attributes.CON,
                "POW": self.attributes.POW,
                "DEX": self.attributes.DEX,
                "APP": self.attributes.APP,
                "SIZ": self.attributes.SIZ,
                "INT": self.attributes.INT,
                "EDU": self.attributes.EDU
            }

            valuesHalf = {
                "STR": self.attributes.STR // 2,
                "CON": self.attributes.CON // 2,
                "POW": self.attributes.POW // 2,
                "DEX": self.attributes.DEX // 2,
                "APP": self.attributes.APP // 2,
                "SIZ": self.attributes.SIZ // 2,
                "INT": self.attributes.INT // 2,
                "EDU": self.attributes.EDU // 2
            }

            valuesFifths = {
                "STR": self.attributes.STR // 5,
                "CON": self.attributes.CON // 5,
                "POW": self.attributes.POW // 5,
                "DEX": self.attributes.DEX // 5,
                "APP": self.attributes.APP // 5,
                "SIZ": self.attributes.SIZ // 5,
                "INT": self.attributes.INT // 5,
                "EDU": self.attributes.EDU // 5
            }

            valuePerDifficulty = {
                "easy": values.get(attr, 0),
                "normal": valuesHalf.get(attr, 0),
                "hard": valuesFifths.get(attr, 0)
            }

            return roll <= valuePerDifficulty.get(difficulty, 0)

    class Npc:
        def __init__(self, name, img, color):
            self.character = Character(name, color=color)
            self.img = img

        def say(self, text):
            self.character(text)

        def enable(self):
            renpy.hide(self.img)
            renpy.show(self.img, at_list=[enabled])

        def disable(self):
            renpy.hide(self.img)
            renpy.show(self.img, at_list=[disabled])

        def hide(self):
            renpy.hide(self.img)
