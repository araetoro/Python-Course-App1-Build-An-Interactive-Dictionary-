#load the data set
import difflib
from difflib import get_close_matches
import json
data = json.load(open("data.json"))
#request input key from user and return value

def fetch_word(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input("Did you mean %s ? Press Y for yes or N for no: " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
             return ("Sorry about that we are not sure what word you were looking for")
    else:
        return input("Sorry we couldn't find your word.")

word = input("Please enter a word: ")

output = fetch_word(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
