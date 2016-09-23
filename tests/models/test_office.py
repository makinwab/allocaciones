import unittest
from allocations.models.room import Room
from allocations.models.office import Office

class TestOfficeModel(unittest.TestCase):

    # setup
    def setUp(self):
        self.room = Office()

    def test_instance_is_valid(self):
        self.assertIsInstance(self.room, Office)
        assert issubclass(Office, Room)

    def test_max_spaces(self):
        self.assertEqual(self.room.max_spaces, 6)

    def test_create_creates_office_spaces(self):
        result = self.room.create(["office", "carat", "vvida", "minion"])
        self.assertIn("minion", self.room.spaces)
        self.assertIn("carat", self.room.spaces)
        self.assertIn("vvida", self.room.spaces)

    def test_get_accomodation_allocates_room_to_person(self):
        result = self.room.get_accomodation("bukky")
        self.assertNotEqual(self.room.occupied, [])
