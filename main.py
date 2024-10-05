from room import Room
from character import Enemy
from character import Character
from friend import Friend


kitchen=Room("Kitchen")
ballroom=Room("Ballroom")
dining_hall=Room("Dining Hall")

bob = Character("Bob", "a friendly ghost")
ballroom.set_character(bob)

jane = Friend("Jane", "a kind-hearted fairy")
dining_hall.set_character(jane)

dave=Enemy("dave", " a smelly zombe")
dave.describe()
dave.set_converstation("how are you")
dave.set_weakness("chees")
# for obj in [dining_hall,ballroom,kitchen]:
#     obj.set_character(dave)
kitchen.set_character(dave)

kitchen.set_description("A dand and dirty room buzzing with flys")
ballroom.set_description(" A greet room")
dining_hall.set_description("a greet dining room")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

current_room= kitchen

# while True:
#     print("\n")
#     current_room.get_details()
#     inhabitant=current_room.get_character()
#     if inhabitant is not None:
#         inhabitant.describe()
#         dave.talk()

#     command=input("> ")
#     current_room=current_room.move(command)

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    # Checks whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    # Talk to the character in the room
    elif command == "talk" and inhabitant is not None:
        inhabitant.talk()

    # Fight the character in the room
    elif command == "fight" and inhabitant is not None:
        print("What will you fight with?")
        fight_with = input("Enter item: ")
        if not inhabitant.fight(fight_with):
            print("Game Over!")
            break  # End the game if you lose the fight
    
    elif command == "hug" and isinstance(inhabitant, Friend):
        inhabitant.hug()

    elif command == "gift" and isinstance(inhabitant, Friend):
        gift = input("What gift would you like to offer? ")
        inhabitant.offer_gift(gift)
    else:
        print("Command not recognized or no inhabitant to interact with.")
