from collections import Counter

class spelling_bee_solver:
    def __init__(self, word_list_file='data/words.txt'):
        self.word_list_file = word_list_file
        self.word_list = self.load_words()
    
    def load_words(self):
        word_list = []
        with open(self.word_list_file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                word_list.append(word)
        print(f"Loaded {len(word_list)} words into the list.")
        return word_list
    
    def find_anagrams(self, letters, required_letter):
        letters = letters.lower()
        required_letter = required_letter.lower()
        letters_count = Counter(letters)
        anagrams = []
        
        for word in self.word_list:
            if len(word) >= 4 and required_letter in word:
                word_count = Counter(word)
                if all(word_count[char] <= letters_count[char] for char in word_count):
                    anagrams.append(word)
                
        return anagrams