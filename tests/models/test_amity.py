import unittest
from models.amity import Amity

class TestAmityModel(unittest.TestCase):

    """
        Set up test data
    """
    def setUp(self):
        self.hostel = Amity()

    """
        Verify is instance of Class is valid
    """
    def test_instance_is_valid(self):
        self.assertIsInstance(self.hostel, Amity, "Invalid instance")
