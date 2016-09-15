from room import Room

class LivingSpace(Room):

    #can accomodate
    max_spaces = 4
    spaces = {}

    def create(self, data):
        rooms = super(LivingSpace, self).create(data)["livingspace"]
        for room in rooms:
            self.spaces[room] = self.max_spaces

        print self.spaces
        print "Living spaces created"

    @classmethod
    def get_accomodation(cls, person):
        self.allocations(person);
