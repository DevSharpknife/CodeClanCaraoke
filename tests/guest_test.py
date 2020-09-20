import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room_2 = Room("Studio 54", 45.00)
        self.guest_1 = Guest("Mick", "Jagger", 20, 12000.00)
        self.guest_2 = Guest("Justin", "Bieber", 16, 0.82)
        self.guest_3 = Guest("Joni", "Mitchell", 21, 100.00)
        self.guest_4 = Guest("Susan", "Boyle", 47, 36.42)
        self.guest_5 = Guest("Courtney", "Love", 31, 666.66)

    def test_customer_has_funds(self):
        self.assertEqual(100.00, self.guest_3.wallet_cash_count())

    def test_remove_cash_from_wallet(self):
        self.guest_1.remove_cash_from_wallet(self.room_2.entry_fee)
        self.assertEqual(11955.00, self.guest_1.wallet_cash_count())