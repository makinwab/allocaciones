from room import Room

class Person(object):

    def __init__(self):
        self.name = None
        self.wants_accommodation = None
        self.role = None

    def add(self, data):
        print data
        self.name = data[0]
        self.role = data[1].upper()
        self.wants_accommodation = data[2].upper()

    def allocate_room(self, office, livingspace):
        if self.role == "FELLOW" and self.wants_accommodation == "Y":
            livingspace.get_accomodation(self.name)
        else:
            #office.get_accomodation(self.name)
            print "allocate office"
