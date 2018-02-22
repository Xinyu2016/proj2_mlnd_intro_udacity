import webbrowser
class Vedio():
    def __int__(self,title,duration,director):
        self.title = title
        self.duration = duration
        self.director = director

class Movie(Vedio):
    def __init__(self,title,duration,director,imbd_link,movie_storyline,poster_image,trailer_youtube):
        #Vedio.__init__(self,title,duration)
        self.title = title
        self.duration = duration
        self.director = director
        self.imbd_link = imbd_link
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)

class TvShow():
    def __int__(self,title,duration,season,episode,tv_station):
        #Vedio.__init__(self,title,duration)
        #self.title = title
        #self.duration = duration
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        print (self.tv_station)


