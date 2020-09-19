import unittest

from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        
        self.song_1 = Song("Juice", "Lizzo")
        self.song_list = [self.song_1]

        self.room_1 = Room("Bowie", self.song_list)

    def test_room_has_name(self):
        self.assertEqual("Bowie", self.room_1.name)

    def test_song_count(self):
        self.assertEqual(1, len(self.song_list))

    # def test_add_song_to_song_list(self):
    #     self.add_song_to_song_list(self.song_1)
    #     self.assertEqual(1, len(self.song_list))