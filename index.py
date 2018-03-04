from finder_interface import FinderInterface
from cleaner import Cleaner
from writer_interface import WriterInterface
from cli_messages import Message

wiki_finder = FinderInterface("World_War_II")
word = wiki_finder.get_word()

cleaner = Cleaner()
clean_word = cleaner.clean(word)

writer = WriterInterface()
writer.save_word(clean_word)

# Game introduction
echo = input("Are you ready to play? ")
print(" ")
name = input("What is your name darling? ")
message = Message(name)

if echo == "yes":
    # Choose the level
    level = input("What is your LEVEL (easy/medium/hard)? ")
    if level == "easy":
        max_turns = len(clean_word) + 10
    elif level == "medium":
        max_turns = len(clean_word) + 6
    elif level == "hard":
        max_turns = len(clean_word) + 2
    else:
        message.incorrect_level()
        max_turns = 10

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

        if writer.is_winner() == True:
            message.success_game(writer.return_full_word())
            turns = max_turns

        turns += 1
else:
    message.cancel_game()
