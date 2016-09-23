import unittest
from allocations.models.amity import Amity

class TestAmityModel(unittest.TestCase):

    """
    Test case for Amity model
    """

    def setUp(self):
        self.hostel = Amity()

    def create_offices(self):
        self.hostel.create_room(["office", "ib", "lagos", "abj"])

    def create_living_spaces(self):
        self.hostel.create_room(["livingspace", "carat", "jm"])

    def tearDown(self):
        del self.hostel.office
        del self.hostel.livingspace

    def get_input(self):
        return "create_room OFFICE lagos"

    def test_instance_is_valid(self):
        self.assertIsInstance(self.hostel, Amity, "Invalid instance")

    def test_create_room_populates_rooms(self):
        self.create_offices()
        self.assertItemsEqual(["ib", "lagos", "abj"], self.hostel.office.spaces)

    def test_add_person_creates_person_and_allocates_room(self):
        self.hostel.office.occupied = {}
        self.create_offices()
        self.hostel.add_person(["bukky", "fellow"])
        self.assertEqual("bukky", self.hostel.fellow.name)
        self.assertTrue(self.hostel.office.occupied)

    def test_add_person_when_want_accomodation_exists(self):
        self.hostel.livingspace.occupied = {}
        self.create_offices()
        self.create_living_spaces()
        self.hostel.add_person(["bukky", "fellow", "Y"])
        self.assertTrue(self.hostel.office.occupied)
