from character import Character

class Friend(Character):
    def hug(self):
        print(f"You give {self.name} a big hug!")

    def offer_gift(self, gift):
        print(f"You offer {self.name} a {gift}.")
