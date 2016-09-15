class Room(object):

    rooms = {
        "office": [],
        "livingspace": []
    }

    def create(self, data):
        existing_rooms = self.rooms[data[0]]
        self.rooms[data[0]] = existing_rooms + data[1:]
        #print self.rooms
        return self.rooms
