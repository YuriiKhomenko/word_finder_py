import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def word_finder(word):
  if word.title() in data:  # in case the word starts with capital letter
    return data[word.title()]
  elif word.lower() in data:
    return data[word.lower()]
  elif word.upper() in data: # in case user enters acronyms (USA, NATO, EU etc)
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())) >= 0: # in case we do not find exact word but are able to find words which are similar
    word = get_close_matches(word, data.keys())[0]
    choice = input("Did you mean {}? Press Y/N: ".format(word))
    choice = choice.lower()
    if choice == "yes" or choice == "y":
      return data[word]
    elif choice == "no" or choice == "n":
      return "See you next time :)"
  else:
    return "We didn't find such word. Try another one" # we didn't find any word that matches with the input

word = input("Please enter a word: ")

output = word_finder(word)
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
