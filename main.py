"""
Author: Rokib
Purpose: List all the pets and allow the customer to
          see information about a chosen pet, continue, edit, or quit.
"""
import pymysql.cursors
from creds import *
from pets import *

petsDict = {}

def listChoices():
    print("*".center(30, "*"))
    print(" Pet Chooser ".center(30, "*"))
    print("*".center(30, "*"))
    for petId in petsDict:
        print(f"[{petId}] {petsDict[petId].getPetName()}")
    print("Enter Q to Quit")

try:
    connection = pymysql.connect(
        host=host, user=username, password=password, db=database,
        charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
    )
except Exception as e:
    print("An error has occurred.  Exiting.")
    print(e)
    exit()

try:
    with connection.cursor() as cursor:
        sql = """
        SELECT
            pets.id AS id, pets.name AS pet, pets.age,
            owners.name AS owner, types.animal_type AS animal
        FROM pets
        JOIN owners ON pets.owner_id = owners.id
        JOIN types ON pets.animal_type_id = types.id;
        """
        cursor.execute(sql)
        for row in cursor:
            tempPet = Pet(
                petId=row['id'], animalType=row['animal'],
                ownerName=row['owner'], petAge=row['age'], petName=row['pet']
            )
            petsDict[row['id']] = tempPet
except Exception as e:
    print("An error has occurred. Exiting.")
    print(e)
finally:
    connection.close()

def editPet(petId):
    pet = petsDict[petId]
    print(f"\nYou have chosen to edit {pet.getPetName()}.")

    new_name = input("New name: [ENTER == no change] ")
    if new_name.strip().lower() == 'quit':
        print("Quit without saving changes.")
        return
    if new_name:
        pet.petName = new_name
        print(f"Pet's name has been updated to {new_name}.")

    try:
        new_age = input("New age: [ENTER == no change] ")
        if new_age.strip().lower() == 'quit':
            print("Quit without saving changes.")
            return
        if new_age:
            new_age = int(new_age)
            pet.petAge = new_age
            print(f"Pet's age has been updated to {new_age}.")
    except ValueError:
        print("Invalid age. Age not updated.")

def main():
    while True:
        listChoices()
        pet = input("Please choose from the list above: ")

        if pet.upper() == "Q":
            print("Thank you.")
            break

        try:
            petId = int(pet)
            if petId in petsDict:
                tempPet = petsDict[petId]
                print(
                    f"\nYou have chosen {tempPet.getPetName()}, the {tempPet.getAnimalType()}. "
                    f"{tempPet.getPetName()} is {tempPet.getPetAge()} years old. "
                    f"{tempPet.getPetName()}'s owner is {tempPet.getOwnerName()}.\n"
                )

                while True:
                    action = input("Would you like to [C]ontinue, [Q]uit, or [E]dit this pet? ").upper()
                    if action == "Q":
                        print("Thank you.")
                        return
                    elif action == "C":
                        break
                    elif action == "E":
                        editPet(petId)
                        break
                    else:
                        print("Invalid choice. Please choose C, Q, or E.")
            else:
                print(f"There is no pet with ID {pet}.")
        except ValueError:
            print(f"It appears that '{pet}' is not a Pet ID or 'Q'")
        except Exception as e:
            print(f"{pet} is an invalid choice")
            print(f"Error message: {e}")

if __name__ == "__main__":
    main()
