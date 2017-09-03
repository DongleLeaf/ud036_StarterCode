import webbrowser


class Movie():
    # define init function
    def __init__(self, movie_title, movie_year,
                 movie_storyline, movie_starring, poster_image,
                 my_rating, trailer_youtube):
        # movie's title
        self.title = movie_title
        # the year when movie release
        self.year = movie_year
        # movie's basic story line
        self.storyline = movie_storyline
        # the star of this movie
        self.starring = movie_starring
        # movie's main poster image
        self.poster_image_url = poster_image
        # my rating for this movies
        self.rating = my_rating
        # movie's main trailer
        self.trailer_youtube_url = trailer_youtube

    # define show_trailer function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
