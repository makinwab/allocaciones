from docopt import docopt
from person import Person
from office import Office
from living_space import LivingSpace

class Amity(object):

    def __init__(self):
        print "Welcome to Amity\n"
        self.person = Person()
        self.office = Office()
        self.livingspace = LivingSpace()

    def ready(self):
        # command = None
        # while command != "exit":
        command = self.get_input()
        method_params = map(str.lower, command.split())
        getattr(self, method_params[0])(method_params[1::])


    def get_input(self):
        return raw_input("What do you want to do?\n").strip()

    """
     create_room OFFICE carat vvida minion
     create_room LIVINGSPACE carat vvida minion
    """
    def create_room(self, rooms):
        if rooms[0] == "office":
            self.office.create(rooms)
        else:
            self.livingspace.create(rooms)

    """
    add_person bukky FELLOW Y
    add_person jay STAFF
    """
    def add_person(self, details):
        self.person.add(details)

if __name__ == '__main__':
    amity = Amity()
    amity.ready()
