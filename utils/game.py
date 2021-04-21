
from random import choice



class Hangman():
    def __init__(self, words):
        self.possible_words = words
        self.word = choice(self.possible_words).upper()
        self.lives = 5
        self.errors = 0
        self.correctly_guessed_letters = "_" * len(self.word)
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    
    def __repr__(self):
        return f"This is a game of hangman word is {''.join(self.word)}"
    
    def start_game(self):
        self._play()
        if self.lives == 0:
            self._game_over()        
        print(self.word, self.correctly_guessed_letters)
        if self.word == self.correctly_guessed_letters:
            self._well_played()

    def _play(self):
        print("Let's Play Hangman!!!\n")
        while self.lives > 0 and self.word != self.correctly_guessed_letters:
            print(f"You have {self.lives} guesses left")
            print("Please enter one letter from below")
            print(self.alphabet)
            print(self.word)
            print(f"The Word: {self.correctly_guessed_letters}")
            guess = input("").upper()
            if len(guess) ==  1 and guess.isalpha():
                if guess not in self.alphabet:
                    print(f"Letter {guess} has been evoked already")
                elif guess not in self.word:
                    self.lives -= 1
                    self.errors += 1
                    self.alphabet.remove(guess)
                else:
                    print(f"{guess} is in the word")
                    self.alphabet.remove(guess)
                    ls = list(self.correctly_guessed_letters)
                    indexes = [i for i, letter in enumerate(self.word) if letter == guess]
                    for i in indexes:
                        ls[i] = guess
                    self.correctly_guessed_letters = "".join(ls)
            
    
    def _game_over(self):
        print(f"You lost, the word was {self.word}.")
        play_again = input("Care to play again? [Y/N]\n").lower()
        if play_again == "y":
            self.reset()
        else:
            print("Thanks for playing")

    def _well_played(self):
        print("Bravo, you won!")
        print(f"You have done {self.errors} mistakes")
        play_again = input("Care to play again? [Y/N]\n").lower()
        if play_again == "y":
            self.reset()
        else:
            print("Thanks for playing")

    def reset(self):
        self.word = choice(self.possible_words).upper()
        self.lives = 5
        self.errors = 0
        self.correctly_guessed_letters = "_" * len(self.word)
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.start_game()





