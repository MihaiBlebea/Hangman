from finder_interface import FinderInterface
from cleaner import Cleaner
from writer_interface import WriterInterface


wiki_finder = FinderInterface("World_War_II")
word = wiki_finder.get_word()

cleaner = Cleaner()
clean_word = cleaner.clean(word)

writer = WriterInterface()
writer.save_word(clean_word)

echo = input("Are you ready to play? ")
print(" ")

if echo == "yes":
    name = input("What is your name darling?")
    print(" ")
    print("Let's play then...")
    print(" ")

    max_turns = 10
    turns = 0
    while turns < max_turns:
        print("This is your word: " + writer.return_word())
        letter = input("[Turn " + str(turns) + "]: Next letter:")
        print(" ")

        writer.guess_letter(letter)
        if writer.is_winner() == True:
            print("Very good " + name + ", you won!!!")
            print("The word was " + writer.return_full_word())
            turns = max_turns

        turns += 1
else:
    print("Oki, no worries")
