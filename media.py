import webbrowser
class Movie():
  #create constructor method
  def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
    #instance variables
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self,): #instance method
    webbrowser.open(self.trailer_youtube_url)