
# app.py
import streamlit as st
from solver import spelling_bee_solver
from collections import defaultdict

def main():
    st.title("Spelling Bee Solver")
    st.write("Enter a group of letters and a required letter to find words containing these letters with more than 4 letters and including the specific letter.")
    
    solver = spelling_bee_solver()
    
    letters = st.text_input("Letters", max_chars=20)
    required_letter = st.text_input("Required Letter", max_chars=1)
    
    if st.button("Find Words"):
        if letters and required_letter:
            st.write(f"Searching for words containing letters: {letters} and including the letter: {required_letter}")
            anagrams = solver.find_anagrams(letters, required_letter)
            if anagrams:
                # Group words by length
                grouped_anagrams = defaultdict(list)
                for word in anagrams:
                    grouped_anagrams[len(word)].append(word)
                
                # Sort keys in descending order
                sorted_lengths = sorted(grouped_anagrams.keys(), reverse=True)
                
                # Display results
                for length in sorted_lengths:
                    st.write(f"**Words with {length} letters:**")
                    st.write(", ".join(grouped_anagrams[length]))
            else:
                st.write(f"No words found containing letters from '{letters}' with more than 4 letters and including '{required_letter}'")
        else:
            st.write("Please enter both the letters and the required letter.")

if __name__ == "__main__":
    main()
