class music():
    def __init__(self,artist,song,album,year) -> None:
        self.artist=artist
        self.song=song
        self.album=album
        self.year=year

    def __str__(self) -> str:
        return f"Performer: {self.artist}\nSong: {self.song}\nAlbum: {self.album}\nYear: {self.year}"

song1=music("Edsharan","pieśni staropolskie","ludowe",2000)
print(song1)