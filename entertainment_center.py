import fresh_tomatoes

import media


# Avator movie information

order_of_phoenix = media.Movie("Harry Potter: Order of the Phoenix",
                               "Now in his fifth year at Hogwarts, Harry (Daniel Radcliffe)\
                               learns that many in the wizarding community do not know the\
                               truth of his encounter with Lord Voldemort.",
                               "https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg", # NOQA
                               "https://youtu.be/y6ZW7KXaXYk")


# print(avatar.storyline)
# avatar.show_trailer()
# Iron Man movie information

iron_man = media.Movie("Iron Man",
                       "A billionaire industrialist and genius inventor,Tony Stark,\
                       is conducting weapons tests overseas, but terrorists kidnap\
                       him to force him to build a devastating weapon. Instead,\
                       he builds an armored suit and upends his captors. ",
                       "http://x.annihil.us/u/prod/marvel/i/mg/b/c0/4bc5c7b0e371a.jpg", # NOQA
                       "https://youtu.be/DTqa-NEwUbs")

# iron_man.show_trailer()

# Harry Potter and the Halfblood Prince movie information

harry_potter = media.Movie("Harry Potter: Half-Blood Prince",
                           "As Death Eaters wreak havoc in both Muggle and Wizard worlds,\
                           Hogwarts is no longer a safe haven for students. Though Harry\
                           (Daniel Radcliffe) suspects there are new dangers lurking within\
                           the castle walls, Dumbledore is more intent than ever on preparing\
                           the young wizard for the final battle with Voldemort.",
                           "https://upload.wikimedia.org/wikipedia/en/6/68/Harry_Potter_and_the_Half-Blood_Prince_%28video_game%29.jpg", # NOQA
                           "https://youtu.be/5ywxgP9OudI")

# Avengers movie information

avengers = media.Movie("The Avengers",
                       "When Thor's evil brother, Loki, gains access to the\
                       unlimited power of the energy cube called the Tesseract, Nick Fury,\
                       director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat\
                       the unprecedented threat to Earth. Joining Fury's 'dream team' are Iron Man,\
                       Captain America, the Hulk, Thor, the Black Widow and Hawkeye.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", # NOQA
                       "https://youtu.be/eOrNdBpGMv8")

# Batman movie information

batman_begins = media.Movie("Batman Begins",
                            "A young Bruce Wayne travels to the Far East, where he's\
                            trained in the martial arts by Henri Ducard, a member of the\
                            mysterious League of Shadows. When Ducard reveals the League's true purpose,\
                            the complete destruction of Gotham City, Wayne returns to Gotham intent\
                            on cleaning up the city without resorting to murder. With the help of Alfred,\
                            his loyal butler, and Lucius Fox, a tech expert at Wayne Enterprises, Batman is born.",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg", # NOQA
                            "https://youtu.be/vak9ZLfhGnQ")

# Star Wars movie information

star_wars_force_awakens = media.Movie("Star Wars the Force Awakens",
                                      "Thirty years after the defeat of the Galactic Empire, the galaxy faces\
                                      a new threat from the evil Kylo Ren and the First Order. When a defector\
                                      named Finn crash-lands on a desert planet, he meets Rey, a tough scavenger whose\
                                      droid contains a top-secret map. Together, the young duo joins forces with\
                                      Han Solo to make sure the Resistance receives the intelligence\
                                      concerning the whereabouts of Luke Skywalker, the last of the Jedi Knights.",
                                      "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", # NOQA
                                      "https://youtu.be/sGbxmsDFVnE")


# Create a list of movies to be displayed in web page

movies = [order_of_phoenix, iron_man, harry_potter,
          avengers, batman_begins, star_wars_force_awakens]
fresh_tomatoes.open_movies_page(movies)
