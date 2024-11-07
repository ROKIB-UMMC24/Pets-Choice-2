"""
Author: Rokib
Purpose: Pet class
   Five properties with getter and setter methods
   * Animal ID
   * Animal Type
   * Owner Name
   * Pet's Age
   * Pet's Name
"""


class Pet:
    """
     Private properties
    """
    __petId = 1
    __animalType = "dog"
    __ownerName = "John Doe"
    __petAge = 0
    __petName = "Spot"

    def __init__(self,
                 petId=1,
                 animalType="dog",
                 ownerName="John Doe",
                 petAge=0,
                 petName="Spot"):
        """
        Class instantiator

        :param petId: Pet's ID
        :type petId: int
        :param animalType: Type of animal
        :type animalType: str
        :param ownerName: Pet's owner's name
        :type ownerName: str
        :param petAge: Pet's age
        :type petAge: int
        :param petName: Pet's name
        :type petName: str
        """
        self.setPetId(petId)
        self.setAnimalType(animalType)
        self.setOwnerName(ownerName)
        self.setPetAge(petAge)
        self.setPetName(petName)

    def getAnimalType(self):
        """
        Getter for the __animalType property

        :return:
        :rtype:
        """
        return (self.__animalType)

    def setAnimalType(self, animalType):
        """
        Setter for the __animalType property

        :param animalType: Type of animal
        :type animalType: str
        """
        try:
            """
             Is the argument not empty?
            """
            if animalType:
                self.__animalType = animalType

        except Exception as e:
            raise TypeError(f"AnimalType seems to be empty!")

    def getOwnerName(self):
        """
        Getter for the __owner property

        :return:
        :rtype:
        """
        return (self.__owner)

    def setOwnerName(self, owner):
        """
        Setter for the __onwer property

        :param owner: Pet's owner's name
        :type owner: str
        """
        try:
            """
             Is the argument not empty?
            """
            if owner:
                self.__owner = owner

        except Exception as e:
            raise TypeError(f"Owner seems to be empty!")

    def getPetAge(self):
        """
        Getter for the __petAge property

        :return:
        :rtype:
        """
        return (self.__petAge)

    def setPetAge(self, petAge):
        """
        Setter for the __petAge property

        :param petAge: Pet's age
        :type petAge: int
        """
        try:
            """
             Is the argument not empty?
            """
            if int(petAge):
                self.__petAge = petAge

        except Exception as e:
            raise TypeError(f"{petAge} does not look like an integer!")

    def getPetId(self):
        """
        Getter for the __petId property

        :return:
        :rtype:
        """
        return (self.__petId)

    def setPetId(self, petId):
        """
        Setter for the __petId property

        :param petId: Pet's ID
        :type petId: int
        """
        try:
            """
             Is the argument not empty?
            """
            if int(petId):
                self.__petId = petId

        except Exception as e:
            raise TypeError(f"{petId} does not look like an integer!")

    def getPetName(self):
        """
        Getter for the __petName property

        :return:
        :rtype:
        """
        return (self.__petName)

    def setPetName(self, petName):
        """
        Setter for the __petName property

        :param petName: Pet's name
        :type petName: str
        """
        try:
            """
             Is the argument not empty?
            """
            if petName:
                self.__petName = petName

        except Exception as e:
            raise TypeError(f"PetName seems to be empty!")