import urllib.request as urllib
from bs4 import BeautifulSoup
import random

class Finder:

    base_url = "https://en.wikipedia.org/wiki/"

    container_el = { "element": "div", "class": "mw-parser-output" }

    paragraph_el = { "element": "p", "class": "" }

    def __init__(self, url):
        self.url = self.base_url + url

    def soup(self):
        page = urllib.urlopen(self.url)
        soup = BeautifulSoup(page, "html.parser")
        return soup

    def find_paragraph(self, soup):
        main = soup.find(self.container_el["element"], attrs = {"class": self.container_el["class"]})
        paragraphs = main.findAll(self.paragraph_el["element"], attrs = {"class": self.paragraph_el["class"]})
        paragraphs_count = len(paragraphs)

        random_int = self.random_int(paragraphs_count)

        for index, paragraph in enumerate(paragraphs):
            if index == random_int:
                return paragraph.text

    def find_word(self, paragraph):
        words = paragraph.split(" ")
        words_count = len(words)

        random_int = self.random_int(words_count)

        for index, word in enumerate(words):
            if index == random_int:
                return word

    # Auxiliar methods to help
    def random_int(self, maxim):
        return random.randint(0, maxim)
