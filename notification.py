import requests


class Notification:
    def __init__(self):
        self.__chat_id = 5850732259
        self.__TOKEN = "5755337602:AAHgyr1dbANnLRU9j2m17GxwAUND_ExLjKs"


    def send_notification(self,message):
        self.__chat_id = 5850732259
        url = f"https://api.telegram.org/bot{self.__TOKEN}/sendMessage?chat_id={self.__chat_id}&text={message}"
        print(requests.get(url).json())  # this sends the message
        self.__chat_id = 5618823220
        url = f"https://api.telegram.org/bot{self.__TOKEN}/sendMessage?chat_id={self.__chat_id}&text={message}"   #niki
        print(requests.get(url).json())  # this sends the message


