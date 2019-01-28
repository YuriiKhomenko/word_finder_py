import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def word_finder():
  word = input("Please enter a word: ")
  word = str(word)
  word = word.lower()
  if word in data:
    return data[word]
  elif len(get_close_matches(word, data.keys(), cutoff=0.8)):
    word = get_close_matches(word, data.keys(), cutoff=0.8)[0]
    choice = input("Did you mean {}? Press Y/N: ".format(word))
    choice = str(choice)
    choice = choice.lower()
    if choice == "yes" or choice == "y":
      return data[word]
    else:
      return "See you next time :)"
  else:
    choice = input("We didn't find such word :( Do you want to look for another word? (Y/N) ")
    if choice == "yes" or choice == "y":
      print(word_finder())
    else:
      return "See you next time :)"

print(word_finder())
