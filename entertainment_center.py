import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        81,
                        "John Lasseter",
                        "http://www.imdb.com/title/tt0114709/",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

Spider_Man = media.Movie("Spider-Man: Homecoming",
                        136,
                         "Jon Watts",
                         "http://www.imdb.com/title/tt2250912/",
                        "Thrilled by his experience with the Avengers, young Peter Parker returns home to live with his Aunt May.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Spider-Man_Homecoming_poster.jpg/220px-Spider-Man_Homecoming_poster.jpg",
                        "https://www.youtube.com/watch?v=fBlzU067ZDU"
                        )

Wonder_Woman = media.Movie("Wonder Woman",
                        141,
                        "Patty Jenkins",
                        "http://www.imdb.com/title/tt0451279/",
                        "In present-day Paris, Diana Prince receives a photographic plate of herself and four men taken during World War I, prompting her to recall her past.",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
                        "https://www.youtube.com/watch?v=1Q8fG0TtVAY"
                        )

Planet_of_Apes = media.Movie("War for the Planet of the Apes",
                        140,
                        "Matt Reeves",
                        "http://www.imdb.com/title/tt3450958/",
                        "It is the third installment in the Planet of the Apes reboot series.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",
                        "https://www.youtube.com/watch?v=qxjPjPzQ1iU"
                        )

Get_Out = media.Movie("Get Out",
                        104,
                        "Jordan Peele",
                        "http://www.imdb.com/title/tt5052448/",
                        "Now that Chris and his girlfriend, Rose, have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean.",
                        "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                        "https://www.youtube.com/watch?v=DzfpyUB60YY"
                        )

Logan = media.Movie("Logan",
                        137,
                        "James Mangold",
                        "http://www.imdb.com/title/tt3315342/",
                        "In the near future, a weary Logan  cares for an ailing Professor X at a remote outpost on the Mexican border.",
                        "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                        "https://www.youtube.com/watch?v=RH3OxVFvTeg"
                        )


movies = [toy_story,Spider_Man,Wonder_Woman,Planet_of_Apes,Get_Out,Logan]

fresh_tomatoes.open_movies_page(movies)