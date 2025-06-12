transform enabled:
    matrixcolor BrightnessMatrix(0)

transform disabled:
    matrixcolor BrightnessMatrix(-0.5)

init python:
    import random

    class Dice:
        @staticmethod
        def rollD100():
            return renpy.display_menu([("Jogar D100", random.randint(1, 100))])

        @staticmethod
        def rollD6():
            return renpy.display_menu([("Jogar D6", random.randint(1, 6))])

    class Player:
        def __init__(self):
            self.name = ""
            self.maxHealthPoints = 0
            self.maxSanityPoints = 0
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

            if self.healthPoints < 0:
                self.healthPoints = 0

        def restoreHealth(self, amount):
            self.healthPoints += amount

            if self.healthPoints > self.maxHealthPoints:
                self.healthPoints = self.maxHealthPoints

        def takeSanityDamage(self, amount):
            self.sanityPoints -= amount

            if self.sanityPoints < 0:
                self.sanityPoints = 0

        def restoreSanity(self, amount):
            self.sanityPoints += amount

            if self.sanityPoints > self.maxSanityPoints:
                self.sanityPoints = self.maxSanityPoints

        def setAttributes(self, attrs):
            self.attributes.STR = int(attrs["playerSTR"])
            self.attributes.CON = int(attrs["playerCON"])
            self.attributes.POW = int(attrs["playerPOW"])
            self.attributes.DEX = int(attrs["playerDEX"])
            self.attributes.APP = int(attrs["playerAPP"])
            self.attributes.SIZ = int(attrs["playerSIZ"])
            self.attributes.INT = int(attrs["playerINT"])
            self.attributes.EDU = int(attrs["playerEDU"])
            self.healthPoints = (self.attributes.SIZ + self.attributes.CON) // 10
            self.sanityPoints = self.attributes.POW
            self.magicPoints = self.attributes.POW // 5

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

        def reset(self):
            self.attributes.STR = 0
            self.attributes.CON = 0
            self.attributes.POW = 0
            self.attributes.DEX = 0
            self.attributes.APP = 0
            self.attributes.SIZ = 0
            self.attributes.INT = 0
            self.attributes.EDU = 0
            self.healthPoints = 0
            self.sanityPoints = 0
            self.magicPoints = 0

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
