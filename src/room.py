class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.song_list = []
        self.guest_list = []

    def get_room_name(self):
        return self.name

    
    def get_song_list(self):
        return self.song_list


    def get_guest_list(self):
        return self.guest_list


    def change_room_name(self, new_room_name):
        self.name = new_room_name

    
    def song_count(self):
        return len(self.song_list)
        

    def add_song_to_list(self, song):
        self.song_list.append(song)

    def remove_song_from_list(self, song):
        self.song_list.remove(song)