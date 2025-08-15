import random

class Word_Game:

    def get_random_word(self):
        """Get a random word from the secret word."""
        word_list = ["education", "student", "software", "program",
                     "laptop", "engineer", "develop", "masters"]
        return random.choice(word_list)

    def display_blanks(self, word):
        """Display the blanks list for the secret word."""
        return ['_' for _ in word]

    def check_letter(self, word, letter, blanks):
        """Check if the letter in the word is in the secret word."""
        search_exist = False
        for i, letr in enumerate(word):
            if letr == letter:
                blanks[i] = letter
                search_exist = True
        return search_exist

    def all_blanks_filled(self, blanks):
        """Check if all blanks are filled."""
        return "_" not in blanks

    def play_game(self):
        """Play a game of guessing game."""
        print("\nWelcome to The Word Guessing Game!")
        word = self.get_random_word()
        print(f"\nTip: The word has {len(word)} characters.")
        blanks = self.display_blanks(word)
        print(blanks)
        used = set()
        lives = 5
        while ( lives > 0 ):
            letter = input("\nPlease select a letter to guess :").strip().lower()
            used.add(letter)
            if self.check_letter(word,letter,blanks):
                print(f"\nYou guessed a correct letter.")
                print(" ".join(blanks))
                if self.all_blanks_filled(blanks):
                    print("\nCongratulations! \nYou guessed the word!")
                    print(f"Word is {word}")
                    break
            else:
                print("Sorry, that's not a valid letter.")
                lives -= 1
                print(f"You have {lives} more chances")

        if lives == 0:
            print("\nYou didn't guess the word.")
            print(f"Word is {word}")
            print("Game over!")

if __name__ == '__main__':
    game = Word_Game()
    game.play_game()
