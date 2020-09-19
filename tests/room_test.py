import unittest

from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Bowie")

    def test_room_has_name(self):
        self.assertEqual("Bowie", self.room_1.name)

    def test_add_song_to_song_list(self):
        self.assertEqual(1, len(self.room.song_list))