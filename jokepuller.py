import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

"""
This class pulls the jokes from https://parade.com/968666/parade/chuck-norris-jokes/

It initially downloads all the jokes into a list and then sends them from that list
(to only scrape once instead at every request). 

"""


class JokePuller:
    __jokes=[]

    """
    Initiates the jokes list
    """
    def __init__(self):
        url = "https://parade.com/968666/parade/chuck-norris-jokes/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all('li'):
            if('Chuck' in tag.text or 'Norris' in tag.text):
                self.__jokes.append(tag.text)


    """
    returns that <id>'th joke from jokes
    """
    def gimme(self,id):
        return "#"+str(id)+": " + self.__jokes[id-1]
