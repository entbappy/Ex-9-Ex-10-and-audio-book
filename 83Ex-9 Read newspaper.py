#Akhbaar padhke sunaoo
import requests
import json
i = 1
def speak(str):

    from win32com.client import Dispatch


    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("News for today.. Lets begin with today's headlines of newses")
    url = "http://newsapi.org/v2/top-headlines?country=" \
          "us&category=science&apiKey=API"

    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_json["articles"])
    art = news_dict["articles"]

    for article in art:
        print(f"Headline number:{i}")
        print(article["title"])
        speak(article["title"])

        speak("Moving on to the next news listen carefully")
        i+=1
    speak("Thanks for listening")
