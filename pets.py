class Pet:
    def __init__(self, petId, animalType, ownerName, petAge, petName):
        self.petId = petId
        self.animalType = animalType
        self.ownerName = ownerName
        self.petAge = petAge
        self.petName = petName

    def getPetName(self):
        return self.petName

    def setPetName(self, new_name):
        self.petName = new_name

    def getAnimalType(self):
        return self.animalType

    def getOwnerName(self):
        return self.ownerName

    def getPetAge(self):
        return self.petAge
