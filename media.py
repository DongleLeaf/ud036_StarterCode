import webbrowser

class Movie():
    
    def __init__(self, movie_title, movie_year, movie_storyline, movie_starring, poster_image, my_rating, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.starring = movie_starring
        self.poster_image_url = poster_image
        self.rating = my_rating
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

