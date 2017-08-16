import media
import fresh_tomatoes

constantine = media.Movie("Constantine",
                          "2005",
                          "Supernatural detective John Constantine helps a policewoman prove her sister's death was not a suicide, but something more.",
                          "Keanu Reeves, Rachel Weisz, Djimon Hounsou",
                          "https://upload.wikimedia.org/wikipedia/en/2/2b/Constantine_poster.jpg",
                          "9.5",
                          "https://www.youtube.com/watch?v=DEa508Xmmio")

avengers = media.Movie("The Avengers",
                       "2012",
                       "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                       "Robert Downey Jr., Chris Evans, Scarlett Johansson",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "8.8",
                       "https://www.youtube.com/watch?v=1hPpG4s3-O4")

iron_man = media.Movie("Iron Man",
                       "2008",
                       "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                       "Robert Downey Jr., Gwyneth Paltrow, Terrence Howard",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "8.6",
                       "https://www.youtube.com/watch?v=bK_Y5LjSJ-Y")

captain_america = media.Movie("Captain America: Civil War",
                              "2016",
                              "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.",
                              "Chris Evans, Robert Downey Jr., Scarlett Johansson",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                              "8.2",
                              "https://www.youtube.com/watch?v=FkTybqcX-Yo")

thor = media.Movie("Thor",
                   "2011",
                   "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
                   "Chris Hemsworth, Anthony Hopkins, Natalie Portman",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2XkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "7.8",
                   "https://www.youtube.com/watch?v=zHUsYlqbuGM")

inception = media.Movie("Inception",
                        "2010",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "9.0",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

matrix = media.Movie("Matrix",
                     "1999",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                     "9.8",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

interstella = media.Movie("Interstellar",
                          "2014",
                          "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                          "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                          "9.6",
                          "https://www.youtube.com/watch?v=Rt2LHkSwdPQ")

dark_knight = media.Movie("The Dark Knight Rises",
                          "2012",
                          "Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
                          "Christian Bale, Tom Hardy, Anne Hathaway",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_.jpg",
                          "9.4",
                          "https://www.youtube.com/watch?v=g8evyE9TuYk")

movies = [constantine, iron_man, thor, avengers, captain_america, inception, matrix, interstella, dark_knight]
fresh_tomatoes.open_movies_page(movies)
