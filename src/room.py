class Room:

    def __init__(self, name):
        self.name = name
        self.song_list = []
        self.guest_list = []

    def get_room_name(self):
        return self.name

    def song_count(self):
        return len(self.song_list)

    def add_song_to_list(self, song):
        self.song_list.append(song)