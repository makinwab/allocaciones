from random import randint

class Room(object):

    def __init__(self):
        self.rooms = None

    def create(self, data):
        self.rooms = data[1:]
        #import pdb; pdb.set_trace()

    def allocate(self, person):
        number = randint(0,len(self.rooms))
        print self.rooms[number]
