from person import Person

class Fellow(Person):

    accomodations = None
    role = None

    def get_accomodation(self, person):
        print person
        LivingSpace().get_accomodation(person)
