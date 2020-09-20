import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Lizzo", "Juice")
        self.song_2 = Song("Dr Dre", "Forgot About Dre")
        self.song_3 = Song("David Byrne", "Finite=Alright")
        self.song_4 = Song("Portishead", "Glory Box")

    def test_song_has_title(self):
        self.assertEqual("Finite=Alright", self.song_3.song_has_title())

    def test_song_has_artist(self):
        self.assertEqual("Lizzo", self.song_1.song_has_artist())
