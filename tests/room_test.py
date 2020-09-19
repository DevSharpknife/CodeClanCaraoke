import unittest

from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Bowie")
        self.song_1 = Song("Juice", "Lizzo")
        self.song_2 = Song("Dr Dre", "Forgot About Dre")
        self.song_3 = Song("David Byrne", "Finite=Alright")
        self.song_4 = Song("Portishead", "Glory Box")
        self.song_list = [self.song_1, self.song_2, self.song_3]

    def test_room_has_name(self):
        self.assertEqual("Bowie", self.room.name)


    def test_song_count(self):
        self.assertEqual(3, len(self.song_list))
        
    
    def test_add_song_to_list(self):
        self.room.add_song_to_list(self.song_4)
        print(self.song_list)
        self.assertEqual(4, len(self.song_list))