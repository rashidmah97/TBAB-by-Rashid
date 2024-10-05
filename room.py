class Room():
    def __init__(self, room_name):
        self.name=room_name
        self.description=None
        self.linked_room={} #dictionary
        self.character=None
    
    def set_description(self,room_description):
        self.description=room_description

    def get_description(self):
        return self.description

    def ser_name(self,room_name):
        self.name=room_name

    def get_name(self):
        return self.name
    
    def set_character(self,new_character):
        self.character=new_character
    
    def get_character(self):
        return self.character
    
    def link_room(self, room_to_link,direction):
        self.linked_room[direction]=room_to_link

    def get_details(self):
        print(self.name)
        print("---------------------------------------")
        print(self.description)
        for direction in self.linked_room:
            room=self.linked_room[direction]
            print(f"the {room.get_name()} is {direction}")

    def move(self,direction):
        if direction in self.linked_room:
            return self.linked_room[direction]
        else:
            print("you cannot go that way!!")
            return False