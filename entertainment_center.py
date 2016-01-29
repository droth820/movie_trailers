import fresh_tomatoes
import media

#Avator movie information
avatar = media.Movie("Avatar",
                      "The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium,[9][10] a room-temperature superconductor.[11] The expansion of the mining colony threatens the continued existence of a local tribe of Na'vi – a humanoid species indigenous to Pandora. The film's title refers to a genetically engineered Na'vi body with the mind of a remotely located human that is used to interact with the natives of Pandora.",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://youtu.be/EPTHpG7ovak")

#print(avatar.storyline)
#avatar.show_trailer()
#Iron Man movie information
iron_man = media.Movie("Iron Man",
                        "A billionaire industrialist and genius inventor, Tony Stark, is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. ",
                        "http://x.annihil.us/u/prod/marvel/i/mg/b/c0/4bc5c7b0e371a.jpg",
                        "https://youtu.be/DTqa-NEwUbs")

#iron_man.show_trailer()

#Harry Potter and the Halfblood Prince movie information
harry_potter = media.Movie("Harry Potter and the Half-Blood Prince",
                            "As Death Eaters wreak havoc in both Muggle and Wizard worlds, Hogwarts is no longer a safe haven for students. Though Harry (Daniel Radcliffe) suspects there are new dangers lurking within the castle walls, Dumbledore is more intent than ever on preparing the young wizard for the final battle with Voldemort. Meanwhile, teenage hormones run rampant through Hogwarts, presenting a different sort of danger. Love may be in the air, but tragedy looms, and Hogwarts may never be the same again.",
                            "https://upload.wikimedia.org/wikipedia/en/6/68/Harry_Potter_and_the_Half-Blood_Prince_%28video_game%29.jpg",
                            "https://youtu.be/5ywxgP9OudI")

#Avengers movie information
avengers = media.Movie("The Avengers",
                        "When Thor's evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Fury's 'dream team' are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner).",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                        "https://youtu.be/eOrNdBpGMv8")

#Batman movie information
batman_begins = media.Movie("Batman Begins",
                            "A young Bruce Wayne (Christian Bale) travels to the Far East, where he's trained in the martial arts by Henri Ducard (Liam Neeson), a member of the mysterious League of Shadows. When Ducard reveals the League's true purpose -- the complete destruction of Gotham City -- Wayne returns to Gotham intent on cleaning up the city without resorting to murder. With the help of Alfred (Michael Caine), his loyal butler, and Lucius Fox (Morgan Freeman), a tech expert at Wayne Enterprises, Batman is born.",
                            "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                            "https://youtu.be/vak9ZLfhGnQ")

#Star Wars movie information
star_wars_force_awakens = media.Movie("Star Wars the Force Awakens",
                                      "Thirty years after the defeat of the Galactic Empire, the galaxy faces a new threat from the evil Kylo Ren (Adam Driver) and the First Order. When a defector named Finn crash-lands on a desert planet, he meets Rey (Daisy Ridley), a tough scavenger whose droid contains a top-secret map. Together, the young duo joins forces with Han Solo (Harrison Ford) to make sure the Resistance receives the intelligence concerning the whereabouts of Luke Skywalker (Mark Hamill), the last of the Jedi Knights.",
                                      "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                                      "https://youtu.be/sGbxmsDFVnE")


#Create a list of movies to be displayed in web page
movies = [avatar, iron_man, harry_potter, avengers, batman_begins, star_wars_force_awakens]
fresh_tomatoes.open_movies_page(movies)
