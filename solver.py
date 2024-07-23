from collections import Counter
from itertools import product

class spelling_bee_solver:
    def __init__(self, word_list_file='data/words.txt'):
        self.word_list_file = word_list_file
        self.word_list = self.load_words()
        self.word_set = set(self.word_list)  # Use a set for faster lookup

    def load_words(self):
        with open(self.word_list_file, 'r') as file:
            word_list = [word.strip().lower() for word in file]
        print(f"Loaded {len(word_list)} words into the list.")
        return word_list

    def find_anagrams(self, letters, required_letter):
        letters = letters.lower()
        required_letter = required_letter.lower()
        anagrams = set()

        # Generate all combinations of letters with replacement up to a reasonable length
        max_length = 15  # Adjust this length as necessary
        for length in range(4, max_length + 1):
            for combo in product(letters, repeat=length):
                word = ''.join(combo)
                if required_letter in word and word in self.word_set:
                    anagrams.add(word)

        return list(anagrams)