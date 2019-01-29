import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def word_finder(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif len(get_close_matches(word, data.keys())) >= 0:
    word = get_close_matches(word, data.keys())[0]
    choice = input("Did you mean {}? Press Y/N: ".format(word))
    choice = choice.lower()
    if choice == "yes" or choice == "y":
      return data[word]
    elif choice == "no" or choice == "n":
      return "See you next time :)"
  else:
    return "We didn't find such word. Try another one"

word = input("Please enter a word: ")

output = word_finder(word)
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
