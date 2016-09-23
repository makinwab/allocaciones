import unittest
from allocations.models.person import Person

class TestPersonModel(unittest.TestCase):

    #test set up
    def setUp(self):
        print ("Setting Up")
        self.person_instance = Person()

    # check that a true instance of Person was created
    def test_instance_of_person(self):
        self.assertIsInstance(self.person_instance, Person, "Is not an instance")


if __name__ == '__main__':
    unittest.main()
