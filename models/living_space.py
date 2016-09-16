from room import Room
from random import randint


class LivingSpace(Room):

    #can accomodate
    max_spaces = 4
    spaces = []
    occupied = {}

    def create(self, data):
        rooms = super(LivingSpace, self).create(data)["livingspace"]
        self.spaces = list(set(self.spaces + rooms))
        print "Living spaces created"

    def get_accomodation(self, person):
        if not self.spaces:
            print "No rooms have been created"
            return

        number = randint(0,len(self.spaces) - 1)
        room = self.spaces[number]

        if room in self.occupied and self.occupied[room] == self.max_spaces:
            print "Room is occupied"
        else:
            self.occupied[room] = self.occupied[room] + 1 if room in self.occupied else 1
            print "Room {} assigned to person {}".format(room, person)
