from room import Room

class Office(Room):

    # can accomodate
    max_spaces = 6
    spaces = {}

    def create(self, data):
        rooms = super(Office, self).create(data)["office"]
        for room in rooms:
            self.spaces[room] = self.max_spaces

        print self.spaces
        print "Rooms created"
