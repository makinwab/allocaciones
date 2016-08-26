from docopt import docopt

class Amity(object):

    def __init__(self):
        print "Welcome to Amity\n"
        self.rooms = []

    def ready(self):
        command = self.get_input()
        method_params = map(str.lower, command.split())
        getattr(self, method_params[0])(method_params[1::])
        print self.rooms

    def get_input(self):
        return raw_input("What do you want to do?\n").strip()

    """
    Create rooms based on input
    """
    def create_room(self, rooms):
        self.rooms = rooms

if __name__ == '__main__':
    amity = Amity()
    amity.ready()
