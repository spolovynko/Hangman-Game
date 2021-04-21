from utils.game import Hangman
with open("./utils/words.txt", "r") as words:
            possible_words = words.read().split()
            words.close()

a = Hangman(possible_words)
a.start_game()