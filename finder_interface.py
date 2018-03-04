from finder import Finder

# This class acts as an interface to the Finder implementation class
# To init this class, you need to pass the url (term) to the constructor

class FinderInterface(Finder):

    def get_word(self):
        soup = self.soup()
        paragraph = self.find_paragraph(soup)
        word = self.find_word(paragraph)

        if len(word) < 5:
            paragraph = self.find_paragraph(soup)
            word = self.find_word(paragraph)
        else:
            return word
