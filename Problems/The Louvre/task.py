class Painting:
    place = "museum"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


input_title = input()
input_artist = input()
input_year = int(input())
painting = Painting(input_title, input_artist, input_year)
print(f'"{painting.title}" by {painting.artist} ({painting.year}) hangs in the Louvre.')