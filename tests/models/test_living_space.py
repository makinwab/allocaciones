import unittest
from allocations.models.room import Room
from allocations.models.living_space import LivingSpace

class TestLivingSpaceModel(unittest.TestCase):

    # setup
    def setUp(self):
        self.room = LivingSpace()

    def test_instance_is_valid(self):
        self.assertIsInstance(self.room, LivingSpace)
        assert issubclass(LivingSpace, Room)

    def test_max_spaces(self):
        self.assertEqual(self.room.max_spaces, 4)
