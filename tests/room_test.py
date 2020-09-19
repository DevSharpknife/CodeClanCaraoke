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

    def test_room_has_name(self):
        self.assertEqual("Bowie", self.room.get_room_name())

    
    def test_empty_song_list(self):
        self.room.song_count()
        self.assertEqual(0, self.room.song_count())
        
    
    def test_add_song_to_list(self):
        self.room.add_song_to_list(self.song_3)
        self.assertEqual(1, self.room.song_count())