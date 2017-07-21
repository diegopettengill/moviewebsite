import webbrowser


class Movie:
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube,
                 category,
                 imdb_rating,
                 section):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating
        self.category = category
        self.section = section

    def show_trailer(self):
        """ Show the movie trailer """
        webbrowser.open(self.trailer_youtube_url)
