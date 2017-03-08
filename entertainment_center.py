import fresh_tomatoes
import media

lalaland = media.Movie("La La Land",
                       "People singing 2h straight",
                       "http://www.indiewire.com/wp-content/uploads/2016/08/crhirsww8aad6ty.jpg",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")

hacksaw_ridge = media.Movie("Hacksaw Ridge",
                            "Guy saves a lot of people in war",
                            "http://www.hacksawridge.movie/img/posters/poster01.jpg",
                            "https://www.youtube.com/watch?v=s2-1hz1juBI")

moonlight = media.Movie("Moonlight",
                            "Didnt watched it",
                            "https://pbs.twimg.com/media/C6LCIF3U8AAgHT0.jpg",
                            "https://www.youtube.com/watch?v=9NJj12tJzqc")

logan = media.Movie("Logan",
                            "Guy kills a lot of people with his adamantium claws",
                            "https://observatoriodocinema.bol.uol.com.br/wp-content/uploads/2016/11/logan-1.jpg",
                            "https://www.youtube.com/watch?v=s2-1hz1juBI")


movies = [lalaland, hacksaw_ridge, moonlight, logan]

fresh_tomatoes.open_movies_page(movies)