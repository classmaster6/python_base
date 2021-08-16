import json
from difflib import SequenceMatcher

data = json.load(open("dictionary/data.json"))

def translate(word):
    word = word.lower()
    for key in data:
        percent = SequenceMatcher(None, word, key).ratio()  #SequenceMatcher.ratio() 0-1 how similar the words are
        if percent > .8:                                    #None is whitespace
            word = key
            break
        else:
            continue
        
    if word in data:
        return data[word]
    else:
        return "Word doesn't exist"

word = input("Enter word: ")

print(translate(word))