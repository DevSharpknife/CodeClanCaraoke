import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Bowie")
        self.song_1 = Song("Juice", "Lizzo")
        self.song_2 = Song("Dr Dre", "Forgot About Dre")
        self.song_3 = Song("David Byrne", "Finite=Alright")
        self.song_4 = Song("Portishead", "Glory Box")
        self.guest_1 = Guest("Mick", "Jagger", 20)
        self.guest_2 = Guest("Justin", "Bieber", 16)
        self.guest_3 = Guest("Joni", "Mitchell", 21)
        self.guest_1 = Guest("Susan", "Boyle", 47)

    def test_room_has_name(self):
        self.assertEqual("Bowie", self.room_1.get_room_name())

    def test_room_name_change(self):
        self.room_1.change_room_name("Dylan")
        self.assertEqual("Dylan", self.room_1.get_room_name())

    
    def test_room_has_song_list(self):
        self.assertEqual([], self.room_1.get_song_list())
    
    def test_initial_song_list_count_is_zero(self):
        self.room_1.song_count()
        self.assertEqual(0, self.room_1.song_count())
        
    def test_add_song_to_list(self):
        self.room_1.add_song_to_list(self.song_3)
        self.assertEqual(1, self.room_1.song_count())

    def test_add_song_to_list__multiple_songs(self):
        self.room_1.add_song_to_list(self.song_3)
        self.room_1.add_song_to_list(self.song_2)
        self.room_1.add_song_to_list(self.song_1)
        self.assertEqual(3, self.room_1.song_count())


    def test_remove_song_from_list(self):
        self.room_1.song_list = [self.song_1, self.song_3, self.song_2, self.song_4]
        self.room_1.remove_song_from_list(self.song_4)
        self.assertEqual(3, self.room_1.song_count())

    def test_remove_song_from_list__multiple(self):
        self.room_1.song_list = [self.song_1, self.song_3, self.song_2, self.song_4]
        self.room_1.remove_song_from_list(self.song_1)
        self.room_1.remove_song_from_list(self.song_2)
        self.room_1.remove_song_from_list(self.song_4)
        self.assertEqual(1, self.room_1.song_count())


    def test_room_has_guest_list(self):
        self.assertEqual([], self.room_1.get_guest_list())

    def test_add_guest_to_list(self):
        self.room_1.add_guest_to_list(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())