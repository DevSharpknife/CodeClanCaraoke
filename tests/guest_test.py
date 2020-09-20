import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room_2 = Room("Studio 54", 45.00)
        self.guest_1 = Guest("Mick", "Jagger", 20, 12000.00, "Dead Flowers")
        self.guest_2 = Guest("Justin", "Bieber", 16, 5.00, "Sorry")
        self.guest_3 = Guest("Joni", "Mitchell", 21, 100.00, "Juice")

    def test_guest_has_whole_name(self):
        self.assertEqual("Justin", self.guest_2.get_guest_first_name())
        self.assertEqual("Bieber", self.guest_2.get_guest_surname())

    def test_guest_has_age(self):
        self.assertEqual(20, self.guest_1.get_guest_age())

    def test_guest_has_funds(self):
        self.assertEqual(100.00, self.guest_3.wallet_cash_count())

    def test_remove_cash_from_wallet(self):
        self.guest_1.remove_cash_from_wallet(self.room_2.entry_fee)
        self.assertEqual(11955.00, self.guest_1.wallet_cash_count())

    def test_cheer(self):
        self.cheer()
        self.assertEqual("CHOON!", self.guest_3.cheer())