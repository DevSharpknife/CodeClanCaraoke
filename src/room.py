class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.song_list = []
        self.guest_list = []

    def get_room_name(self):
        return self.name

    def change_room_name(self, new_room_name):
        self.name = new_room_name

    def get_song_list(self):
        return self.song_list
    
    def song_count(self):
        return len(self.song_list)

    def add_song_to_list(self, new_song):
        self.song_list.append(new_song)

    def remove_song_from_list(self, old_song):
        self.song_list.remove(old_song)


    def get_guest_list(self):
        return self.guest_list

    def guest_count(self):
        return len(self.guest_list)
    
    def add_guest_to_list(self, new_guest):
        self.guest_list.append(new_guest)

    def remove_guest_from_list(self, old_guest):
        self.guest_list.remove(old_guest)



