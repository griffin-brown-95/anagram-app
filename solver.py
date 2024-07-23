from collections import Counter
import streamlit as st

class spelling_bee_solver:
    def __init__(self, word_list_file='data/words.txt'):
        self.word_list_file = word_list_file
        self.word_list = self.load_words()
    
    @st.cache_data
    def load_words(_self):
        word_list = []
        with open(_self.word_list_file, 'r') as file:
            for word in file:
                word = word.strip().lower()
                word_list.append(word)
        print(f"Loaded {len(word_list)} words into the list.")
        return word_list
    
    def find_anagrams(self, letters, required_letter):
        letters = letters.lower()
        required_letter = required_letter.lower()
        anagrams = []
        
        for word in self.word_list:
            if len(word) >= 4 and required_letter in word:
                if all(char in letters for char in word):
                    anagrams.append(word)
                
        return anagrams
