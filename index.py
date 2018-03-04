import json
from finder_interface import FinderInterface
from cleaner import Cleaner
from writer_interface import WriterInterface
from cli_messages import Message

''' Get the config object from config/config.txt '''
json_file = open("config/config.txt", "r")
config = json.load(json_file)

''' Get the word from the wikipedia page, pass term from config '''
wiki_finder = FinderInterface(config["wiki_term"])
word = wiki_finder.get_word()

''' Clean the word of special characters and signs '''
cleaner = Cleaner()
clean_word = cleaner.clean(word)

''' Save the word and the validating word in the file / database '''
writer = WriterInterface()
writer.save_word(clean_word)

''' Start the game here '''
echo = input("Are you ready to play? ")
print(" ")
name = input("What is your name darling? ")
message = Message(name)

if echo == "yes":
    # Choose the level
    level = input("What is your LEVEL (easy/medium/hard)? ")
    if level == "easy":
        max_turns = len(clean_word) + config["levels"]["easy"]
    elif level == "medium":
        max_turns = len(clean_word) + config["levels"]["medium"]
    elif level == "hard":
        max_turns = len(clean_word) + config["levels"]["hard"]
    else:
        message.incorrect_level()
        max_turns = config["levels"]["default"]

    # Play the game
    turns = 0
    while turns < max_turns:
        message.this_is_the_word(writer.return_word())
        letter = input("[Turn " + str(turns + 1) + "/" + str(max_turns) + "]: Next letter:")

        guess = writer.guess_letter(letter)
        if guess == True:
            message.success(letter)
        else:
            message.fail()

        failed = writer.failed_letters()
        message.failed_letters(failed)

        if writer.is_winner() == True:
            message.success_game(writer.return_full_word())
            turns = max_turns

        turns += 1

        if turns == max_turns:
            writer.game_over()
else:
    message.cancel_game()
