from room import Room
from random import randint

class Office(Room):

    # can accomodate
    max_spaces = 6
    spaces = []
    occupied = {}

    def create(self, data):
        rooms = super(Office, self).create(data)["office"]
        self.spaces = list(set(self.spaces + rooms))
        print "Offices created"

    def get_accomodation(self, person):
        if not self.spaces:
            print "No offices have been created"
            return

        number = randint(0,len(self.spaces) - 1)
        room = self.spaces[number]

        if room in self.occupied and self.occupied[room] == self.max_spaces:
            print "Office is occupied"
        else:
            self.occupied[room] = self.occupied[room] + 1 if room in self.occupied else 1
            print "Office {} assigned to person {}".format(room, person)
