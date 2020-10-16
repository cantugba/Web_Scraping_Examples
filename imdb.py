import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find('tbody',{"class":"lister-list"}).find_all("tr",limit=10)
print("film adı ve yılı")
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class": "titleColumn"}).find("span").text
    rating = tr.find("td",{"class": "ratingColumn"}).find("strong").text
    print("film adı:"+title)
    print("yapım yılı: "+year)
    print("rating: "+rating)

