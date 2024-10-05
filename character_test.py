from character import Enemy

# dave=Character("dave", " a smelly zombe")
# dave.describe()
# dave.set_converstation("how are you")
# dave.talk()
# dave.fight("can")

dave=Enemy("dave", " a smelly zombe")
dave.describe()
dave.set_converstation("how are you")
dave.talk()
# dave.fight("can")
# dave.set_weakness("kkkkkkk")
# dave.fight("kkkkkkk")

dave.set_weakness("cheese")
print("what will you fight with")
fight_with=input("Enter item here: ")
dave.fight(fight_with)