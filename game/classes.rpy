transform enabled:
    matrixcolor BrightnessMatrix(0)

transform disabled:
    matrixcolor BrightnessMatrix(-0.5)

init python:
    import random

    class Dice:
        def rollD100(self, quantity):
            quantityText = str(quantity)
            result = renpy.display_menu([("Jogar " + quantityText + "D100", self.roll(quantity, 100))])

            if quantity == 1:
                return result[0]
            else:
                return result
        
        def rollD6(self, quantity):
            quantityText = str(quantity)
            result = renpy.display_menu([("Jogar " + quantityText + "D6", self.roll(quantity, 6))])

            if quantity == 1:
                return result[0]
            else:
                return result
        
        def roll(self, times, sides):
            results = []

            for _ in range(times):
                result = random.randint(1, sides)
                results.append(result)

            return results


    class Player:
        def __init__(self):
            self.name = ""
            self.occupation = ""
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
            self.occupation = ""
            self.name = ""

        def testAttribute(self, attr, roll, difficulty="normal"):
            if difficulty == "hard":
                return roll <= attr // 2
            elif difficulty == "extreme":
                return roll <= attr // 5
            else:
                return roll <= attr

        def getAttrValuesText(self, attr):
            value = str(attr)
            half = str(attr // 2)
            fifth = str(attr // 5)

            return "({color=#fef9c2}" + value + "{/color}-{color=#ffb86a}" + half + "{/color}-{color=#ff637e}" + fifth + "{/color})"

    class Npc:
        def __init__(self, name, img, color):
            self.name = name
            self.color = color
            self.img = img
            self.character = Character(name, color=color)

        def say(self, text):
            self.enable()
            self.character(text)

        def enable(self):
            renpy.hide(self.img)
            renpy.show(self.img, at_list=[enabled])

        def disable(self):
            renpy.hide(self.img)
            renpy.show(self.img, at_list=[disabled])

        def hide(self):
            renpy.hide(self.img)

        def updateCharacter(self, newName, newImage, newColor):
            name = self.name
            img = self.img
            color = self.color
            
            if newName:
                name = newName

            if newImage:
                img = newImage

            if newColor:
                character.color = newColor

            self.name = name
            self.color = color
            self.img = img
            self.character = Character(name, color=color)
