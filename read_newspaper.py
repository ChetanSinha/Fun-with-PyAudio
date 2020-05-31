import requests
from win32com.client import Dispatch

def read_it(str):
    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)


if __name__ == '__main__':

    news_collection = {1:"the-times-of-india", 2:"the-hindu", 3:"google-news-in", 4:"espn-cric-info", 5:"bbc-news", 6:"the-new-york-times"}
    print(news_collection)
    for i in range(1, len(news_collection)+1):
        read_it(f'To Select {news_collection[i].replace("-"," ")} enter {i}')

    read_it("Please Enter the Number")
    newspaper_num = int(input("Please Enter the Number:"))
    choosen = news_collection[newspaper_num]

    print("Please Wait while we are connecting...")

    url = ('https://newsapi.org/v2/top-headlines?'
           f'sources={choosen}&'
           'apiKey=431364b36a604734bf1295fcd33ea076')
    response = requests.get(url)

    length_of_article = len(response.json()['articles'])

    read_it(f'You are listening to {choosen.replace("-"," ")}')

    read_it("If you only want to listen headlines press 0, else press 1 to listen to whole news")
    n = int(input("Enter here:"))

    for news in range(length_of_article):

        headings = (response.json()['articles'][news]['title'])
        print(headings)
        read_it(headings)

        if n == 1:
            body = response.json()['articles'][news]['description']
            print(body)
            read_it(body)
    read_it("Thank you for using our service")




