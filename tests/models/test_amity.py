import unittest
from allocations.models.amity import Amity

class TestAmityModel(unittest.TestCase):

    """
    Test case for Amity model
    """

    def setUp(self):
        self.hostel = Amity()

    def get_input(self):
        return "create_room OFFICE lagos"

    def test_instance_is_valid(self):
        self.assertIsInstance(self.hostel, Amity, "Invalid instance")

    def test_create_method_populates_rooms(self):
        self.hostel.create_room(["office", "ib", "lagos"])
        self.assertEqual(["ib", "lagos"], self.hostel.office.rooms)

    def test_add_person_creates_person_and_allocates_room(self):
        self.hostel.add_person(["bukky", "fellow", "Y"])
        self.assertEqual("bukky", self.hostel.person.name)
        self.assertEqual("FELLOW", self.hostel.person.role)
        self.assertEqual("Y", self.hostel.person.accommodation)
