from docopt import docopt
from room import Room
from person import Person
from office import Office
from living_space import LivingSpace
from staff import Staff
from fellow import Fellow

class Amity(object):

    def __init__(self):
        print "Welcome to Amity\n"
        self.office = Office()
        self.livingspace = LivingSpace()
        self.staff = Staff()
        self.fellow = Fellow()

    def ready(self):
        command = None
        while command != "exit":
            command = self.get_input()
            if command.lower() == "exit":
                command = "exit"
            else:
                method_params = map(str.lower, command.split())
                getattr(self, method_params[0])(method_params[1::])
        return


    def get_input(self):
        return raw_input(">> ").strip()

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
    def add_person(self, person_details):
        if len(person_details) == 2:
            person_details.append("N")

        if person_details[1] == "fellow":
            self.fellow.add(person_details)
            self.fellow.allocate_room(self.office, self.livingspace)
        else:
            self.staff.add(person_details)
            self.staff.allocate_room(self.office)

if __name__ == '__main__':
    amity = Amity()
    amity.ready()
