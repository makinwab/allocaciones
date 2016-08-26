import unittest
from models.amity import Amity

class TestAmityModel(unittest.TestCase):

    """
    Test case for Amity model
    """

    """
        Set up test data
    """
    def setUp(self):
        self.hostel = Amity()

    def get_input(self):
        return "create_room ib lagos"


    """
        Verify is instance of Class is valid
    """
    def test_instance_is_valid(self):
        self.assertIsInstance(self.hostel, Amity, "Invalid instance")

    """
        Verify create_room creates a list of rooms
    """
    def test_create_method_populates_rooms(self):
        self.hostel.create_room(["oyo", "ib", "lagos"])
        self.assertEqual(["oyo", "ib", "lagos"], self.hostel.rooms)
