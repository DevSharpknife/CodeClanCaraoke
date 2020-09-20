class Song:

    def __init__(self, artist, title) :
        self.title = title
        self.artist = artist

    def song_has_title(self):
        return self.title
    
    def song_has_artist(self):
        return self.artist