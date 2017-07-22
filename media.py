import webbrowser


class Movie:
    """
    Behaviour: Initiates a M<ovie object
    Input: Movie properties
    Output: Movie Object
    :param movies:
    :return:
    """
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
        """
        Behaviour: Show the movie trailer
        Input:Movie Object
        Output: Movie trailer url
        :param self:
        :return:
        """
        webbrowser.open(self.trailer_youtube_url)
