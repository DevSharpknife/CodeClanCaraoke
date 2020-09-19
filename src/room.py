class Room:

    def __init__(self, name, song_list):
        self.name = name
        self.song_list = song_list
        self.guest_list = []


    def add_song_to_song_list(self, song):
        self.song_list.append(song)