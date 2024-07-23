from collections import Counter

with open('data\words.txt', 'r') as f:
    dictionary = f.read()

dictionary = [x.lower() for x in dictionary.split('\n')]

print(len(dictionary))