import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Trailer Monkey</title>

    <meta name="description" content="Your favorite movie trailers website">
    <meta name="keywords" content="trailer, trailers, movie trailers, oscar 2017, reviews">
    <meta name="robots" content="index, follow">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400" rel="stylesheet">

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->

      <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container-fluid">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">
                <img src="img/logo.jpg" class="img-responsive logo" title="Trailer Monkey" />
            </a>
          </div>

          <form class="navbar-form navbar-left">
            <div class="form-group">
              <input type="search" id="search" class="form-control" placeholder="Search a movie by title">
            </div>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Submit a trailer</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>
      </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-xs-12">
            <h1 class="section-title">
                <i class="glyphicon glyphicon-time"></i> Latest Trailers
            </h1>
        </div>
        {movie_tiles}

        <div class="col-xs-12">
            <h1 class="section-title secondary">
                Oscar 2017 Nominations
            </h1>
        </div>
        {movie_tiles_oscars}
      </div>
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-xs-12 col-sm-12 col-md-3 col-lg-2 movie-tile text-center" data-title="{movie_title_lowercase}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="poster" style='background: url("{poster_image_url}") no-repeat; background-size: cover;'>
    </div>
    <h1>{movie_title}</h1>
    <span class="rating">
        <i class="glyphicon glyphicon-star-empty"></i> Rating: {rating}
    </span>
    <span class="category">{category}</span>
    <img class="icon-play" src="img/play_icon.png" title="Click to view the trailer!" alt="Click to view the trailer!" />
</div>
'''


# created the latest section movies
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:

        if movie.section == "latest":
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=movie.title,
                movie_title_lowercase=movie.title.lower(),
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                category=movie.category,
                rating=movie.imdb_rating
            )
    return content


# created the latest section movies
def create_movie_tiles_content_oscars(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:

        if movie.section == "oscar":
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=movie.title,
                movie_title_lowercase=movie.title.lower(),
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id,
                category=movie.category,
                rating=movie.imdb_rating
            )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies),
                                                movie_tiles_oscars=create_movie_tiles_content_oscars(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
