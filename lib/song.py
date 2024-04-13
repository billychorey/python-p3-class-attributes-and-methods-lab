class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {} 
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the count each time a new song is created
        Song.count += 1
        
        # Add the genre to the set of genres
        Song.genres.add(genre)
        
        # Add the artist to the set of artists
        Song.artists.add(artist)
        
        # Update the genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Update the artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
