transform enabled:
    matrixcolor BrightnessMatrix(0)

transform disabled:
    matrixcolor BrightnessMatrix(-0.5)

init python:
    import random
    import enum

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

    # 40%, 50%, 50%, 50%, 60%, 60%, 70%, 80%
    # 70%, 60%, 60%, 50%, 50%, 50%, 40%, 40%
    class ArchetypeBuilder:
        @staticmethod
        def buildAntiquarian():
            player = Player()
            player.occupation = PlayerOccupation.ANTIQUARIAN

            player.skills.creditRating = 20
            player.skills.appraise = 70
            player.skills.craft = 50
            player.skills.history = 60
            player.skills.libraryUse = 60
            player.skills.otherLanguages = 40
            player.skills.spotHidden = 50
            player.skills.fastTalk = 50
            player.skills.handguns = 40

            player.attributes.edu = 60
            player.attributes.int = 80
            player.attributes.siz = 70
            player.attributes.dex = 50
            player.attributes.app = 50
            player.attributes.str = 60
            player.attributes.con = 50
            player.attributes.pow = 40

            player.updateStats()
            player.updateSkills()

            return player

        @staticmethod
        def buildDoctor():
            player = Player()
            player.occupation = PlayerOccupation.DOCTOR

            player.skills.creditRating = 30
            player.skills.firstAid = 60
            player.skills.otherLanguages = 40
            player.skills.medicine = 70
            player.skills.biology = 50
            player.skills.pharmacy = 50
            player.skills.psychology = 50
            player.skills.groundPilot = 40
            player.skills.rifles = 60

            player.attributes.edu = 80
            player.attributes.int = 70
            player.attributes.siz = 60
            player.attributes.dex = 50
            player.attributes.app = 50
            player.attributes.str = 50
            player.attributes.con = 60
            player.attributes.pow = 40

            player.updateStats()
            player.updateSkills()

            return player
            
        @staticmethod
        def buildJournalist():
            player = Player()
            player.occupation = PlayerOccupation.JOURNALIST

            player.skills.creditRating = 20
            player.skills.photography = 60
            player.skills.history = 60
            player.skills.libraryUse = 50
            player.skills.ownLanguage = 40
            player.skills.groundPilot = 50
            player.skills.fastTalk = 70
            player.skills.persuade = 50
            player.skills.handguns = 40

            player.attributes.edu = 80
            player.attributes.int = 70
            player.attributes.siz = 60
            player.attributes.dex = 60
            player.attributes.app = 50
            player.attributes.str = 50
            player.attributes.con = 50
            player.attributes.pow = 40

            player.updateStats()
            player.updateSkills()

            return player
            
        @staticmethod
        def buildInvestigator():
            player = Player()
            player.occupation = PlayerOccupation.INVESTIGATOR

            player.skills.creditRating = 20
            player.skills.photography = 60
            player.skills.disguise = 50
            player.skills.law = 50
            player.skills.libraryUse = 40
            player.skills.groundPilot = 40
            player.skills.spotHidden = 70
            player.skills.persuade = 50
            player.skills.handguns = 60

            player.attributes.edu = 70
            player.attributes.int = 80
            player.attributes.siz = 60
            player.attributes.dex = 50
            player.attributes.app = 50
            player.attributes.str = 60
            player.attributes.con = 50
            player.attributes.pow = 40

            player.updateStats()
            player.updateSkills()

            return player

        @staticmethod
        def buildProfessor():
            player = Player()
            player.occupation = PlayerOccupation.PROFESSOR

            player.skills.creditRating = 20
            player.skills.libraryUse = 70
            player.skills.otherLanguages = 60
            player.skills.ownLanguage = 60
            player.skills.fighting = 50
            player.skills.groundPilot = 40
            player.skills.intimidate = 50
            player.skills.handguns = 40
            player.skills.listen = 50

            player.attributes.edu = 80
            player.attributes.int = 70
            player.attributes.siz = 60
            player.attributes.dex = 50
            player.attributes.app = 50
            player.attributes.str = 60
            player.attributes.con = 50
            player.attributes.pow = 40

            player.updateStats()
            player.updateSkills()

            return player

    class PlayerOccupation(enum.Enum):
        ANTIQUARIAN = "Antiquarian"
        DOCTOR = "Doctor"
        JOURNALIST = "Journalist"
        INVESTIGATOR = "Investigator"
        PROFESSOR = "Professor"

    class PlayerAttributes:
        def __init__(self):
            self.str = 0
            self.con = 0
            self.pow = 0
            self.dex = 0
            self.app = 0
            self.siz = 0
            self.int = 0
            self.edu = 0

    class PlayerSkills:
        def __init__(self):
            self.accounting = 5
            self.anthropology = 1
            self.appraise = 5
            self.archaeology = 1
            self.painting = 5
            self.photography = 5
            self.craft = 5
            self.charm = 15
            self.climb = 20
            self.creditRating = 0
            self.cthuluMythos = 0
            self.disguise = 5
            self.dodge = 0
            self.groundPilot = 5
            self.waterPilot = 5
            self.airPilot = 5
            self.electricalRepair = 10
            self.mechanicalRepair = 10
            self.fastTalk = 5
            self.fighting = 25
            self.handguns = 20
            self.rifles = 25
            self.shotguns = 25
            self.firstAid = 30
            self.history = 5
            self.intimidate = 15
            self.persuade = 10
            self.jump = 20
            self.ownLanguage = 0
            self.otherLanguages = 1
            self.law = 0
            self.libraryUse = 0
            self.listen = 0
            self.locksmith = 0
            self.medicine = 0
            self.naturalWorld = 0
            self.navigate = 0
            self.occult = 0
            self.psychoanalysis = 1
            self.psychology = 1
            self.mathematics = 1
            self.cryptograpfy = 1
            self.botany = 1
            self.biology = 1
            self.chemistry = 1
            self.physics = 1
            self.pharmacy = 1
            self.sleightOfHand = 0
            self.spotHidden = 0
            self.stealth = 0
            self.survival = 0
            self.swim = 0
            self.throw = 0
            self.track = 0

    class PlayerStats:
        def __init__(self):
            self.maxHealthPoints = 0
            self.maxSanityPoints = 0
            self.healthPoints = 0
            self.sanityPoints = 0
            self.magicPoints = 0
            self.luckPoints = 0

    class Player:
        def __init__(self):
            self.name = ""
            self.occupation = ""
            self.stats = PlayerStats()
            self.attributes = PlayerAttributes()
            self.skills = PlayerSkills()

        def takeHealthDamage(self, damage):
            self.stats.healthPoints -= damage

            if self.stats.healthPoints < 0:
                self.stats.healthPoints = 0

        def restoreHealth(self, amount):
            self.stats.healthPoints += amount

            if self.stats.healthPoints > self.stats.maxHealthPoints:
                self.stats.healthPoints = self.stats.maxHealthPoints

        def takeSanityDamage(self, amount):
            self.stats.sanityPoints -= amount

            if self.stats.sanityPoints < 0:
                self.stats.sanityPoints = 0

        def restoreSanity(self, amount):
            self.stats.sanityPoints += amount

            if self.stats.sanityPoints > self.stats.maxSanityPoints:
                self.stats.sanityPoints = self.stats.maxSanityPoints

        # Remover criação de ficha do 0 por enquanto
        # def setAttributes(self, attrs):
        #     self.attributes.str = int(attrs["playerSTR"])
        #     self.attributes.con = int(attrs["playerCON"])
        #     self.attributes.pow = int(attrs["playerPOW"])
        #     self.attributes.dex = int(attrs["playerDEX"])
        #     self.attributes.app = int(attrs["playerAPP"])
        #     self.attributes.siz = int(attrs["playerSIZ"])
        #     self.attributes.int = int(attrs["playerINT"])
        #     self.attributes.edu = int(attrs["playerEDU"])

        def updateSkills(self):
            self.skills.dodge += self.attributes.dex // 2
            self.skills.ownLanguage += self.attributes.edu // 2

            if self.attributes.edu >= 60:
                self.skills.mathematics += 20
            elif self.attributes.edu >= 50:
                self.skills.mathematics += 10
            elif self.attributes.edu >= 40:
                self.skills.mathematics += 5

        def updateStats(self):
            self.stats.maxHealthPoints = (self.attributes.siz + self.attributes.con) // 10
            self.stats.maxSanityPoints = self.attributes.pow
            self.stats.healthPoints = self.stats.maxHealthPoints
            self.stats.sanityPoints = self.stats.maxSanityPoints
            self.stats.magicPoints = self.attributes.pow // 5
            self.stats.luckPoints = 0

        def reset(self):
            self.name = ""
            self.occupation = ""
            self.stats = PlayerStats()
            self.attributes = PlayerAttributes()
            self.skills = PlayerSkills()


        def testProperty(self, attr, roll, difficulty="normal"):
            if difficulty == "hard":
                return roll <= attr // 2
            elif difficulty == "extreme":
                return roll <= attr // 5
            else:
                return roll <= attr

        def getPropertyValueText(self, attr, difficulty="normal"):
            if difficulty == "normal":
                return "({color=#fef9c2}" + str(attr) + "{/color})"
            elif difficulty == "hard":
                return "({color=#ffb86a}" + str(attr // 2) + "{/color}"
            elif difficulty == "extreme":
                return "({color=#ff637e}" + str(attr // 5) + "{/color})"

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
