
class Message:

    def __init__(self, name):
        self.name = name

    def lets_play(self):
        print(" ")
        print("Let's play then...")
        print(" ")

    def cancel_game():
        print(" ")
        print("I'm sorry that you are not in the mood to play with me " + self.name + "!")
        print(" ")

    def incorrect_level():
        print(" ")
        print("I'm sorry but you choose an incorrect level, so I choose for you!")
        print(" ")

    def this_is_the_word(self, word):
        print(" ")
        print("This is your word: " + word)
        print(" ")

    def success(self, letter):
        print(" ")
        print("Bravo " + self.name + "! You guessed letter " + letter.upper())
        print(" ")

    def fail(self):
        print(" ")
        print("Sorry " + self.name + "!")
        print(" ")

    def success_game(self, word):
        print(" ")
        print("Very good " + self.name + ", you won!!!")
        print("The word was " + word.upper())
        print(" ")
