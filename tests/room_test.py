import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("CBGB", 25.00)
        self.song_1 = Song("Juice", "Lizzo")
        self.song_2 = Song("Dr Dre", "Forgot About Dre")
        self.song_3 = Song("David Byrne", "Finite=Alright")
        self.song_4 = Song("Portishead", "Glory Box")
        self.guest_1 = Guest("Mick", "Jagger", 20, 12000.00)
        self.guest_2 = Guest("Justin", "Bieber", 16, 0.82)
        self.guest_3 = Guest("Joni", "Mitchell", 21, 100.00)
        self.guest_4 = Guest("Susan", "Boyle", 47, 36.42)
        self.guest_5 = Guest("Courtney", "Love", 31, 666.66)

    def test_room_has_name(self):
        self.assertEqual("CBGB", self.room_1.get_room_name())

    def test_room_name_change(self):
        self.room_1.change_room_name("Bongo Club")
        self.assertEqual("Bongo Club", self.room_1.get_room_name())

    
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

    def test_clear_song_list(self):
        self.room_1.clear_song_list()
        self.assertEqual(0, self.room_1.song_count())


    def test_room_has_guest_list(self):
        self.assertEqual([], self.room_1.get_guest_list())

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())

    def test_check_in_guest__multiple(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.assertEqual(3, self.room_1.guest_count())
    
    def test_check_in_room_full(self):
        self.room_1.guest_list = [self.guest_1, self.guest_3, self.guest_2, self.guest_4]
        self.room_1.check_in_guest(self.guest_5)
        self.assertEqual("GO AWAY COURTNEY, YOU KILLED KURT!!!", self.room_1.check_in_guest(self.guest_5))
        self.assertEqual(4, self.room_1.guest_count())
    

    def test_check_out_guest(self):
        self.room_1.guest_list = [self.guest_1, self.guest_3, self.guest_2, self.guest_4]
        self.room_1.check_out_guest(self.guest_2)
        self.assertEqual(3, self.room_1.guest_count())

    def test_check_out_guest__multiple(self):
        self.room_1.guest_list = [self.guest_1, self.guest_3, self.guest_2, self.guest_4]
        self.room_1.check_out_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_4)
        self.assertEqual(2, self.room_1.guest_count())

    def test_clear_room(self):
        self.room_1.clear_room()
        self.assertEqual(0, self.room_1.guest_count())

    def test_add_cash_to_till(self):
        self.room_1.add_cash_to_till(100)
        self.assertEqual(200, self.room_1.till_count())