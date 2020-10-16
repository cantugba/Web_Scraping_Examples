import requests

class theMoviveDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "c3c08bb5107665da095cabccad03bb0d"

    def getPopulars(self):
        response = requests.get(f" {self.api_url }movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
    
    
movieApi = theMoviveDb()

while True:
    secim = input("1- Popular Movies \n 2-Search Movies\n 3-Exit \n Seçim: ")
    
    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
              print(movie['title'])
        elif secim == "2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
              print(movie['name'])