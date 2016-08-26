import unittest
from models.room import Room
from models.office import Office

class TestOfficeModel(unittest.TestCase):

    # setup
    def setUp(self):
        self.room = Office()

    def test_instance_is_valid(self):
        self.assertIsInstance(self.room, Office)
        assert issubclass(Office, Room)

    def test_max_spaces(self):
        self.assertEqual(self.room.max_spaces, 6)
