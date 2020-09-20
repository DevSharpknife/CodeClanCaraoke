class Room:

    def __init__(self, room_name, entry_fee):
        self.name = room_name
        self.entry_fee = entry_fee
        self.song_list = []
        self.guest_list = []
        self.room_limit = 4
        self.till = 100.00

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

    def clear_song_list(self):
        self.song_list = []


    def get_guest_list(self):
        return self.guest_list

    def guest_count(self):
        return len(self.guest_list)
    
    def check_in_guest(self, new_guest):
        if self.guest_count() >= 4:
            return "GO AWAY COURTNEY, YOU KILLED KURT!!!"
        else:
            self.guest_list.append(new_guest)

    def check_out_guest(self, old_guest):
        self.guest_list.remove(old_guest)

    def clear_room(self):
        self.guest_list = []

