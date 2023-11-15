import string

# Ths function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

def get_dictionary(book):
  dictionary =  {}
  for word in book:
    # If word is in the dictionary add to count
    if (word in dictionary):
      dictionary[word] += 1
    # If word !in the dictionary add it with a count 1
    else:
      dictionary[word] = 1
  return dictionary

def get_four_letter_word_cnt(dictionary):
  four_word_cnt = 0
  for word in dictionary:
    if (len(word) == 4):
      four_word_cnt += 1
  return four_word_cnt

def get_most_common_word(dictionary):
  most_common_word = ""
  most_common_word_cnt = 0
  for word in dictionary:
    if (dictionary[word] > most_common_word_cnt):
      most_common_word_cnt = dictionary[word]
      most_common_word = word
  return most_common_word

def get_words_500(dictionary):
  word_dict_500 = {}
  for word in dictionary:
    if (dictionary[word] >= 500):
      word_dict_500[word] = dictionary[word]
  return word_dict_500
  
#######################-MAIN-###################################
# A collection of lower-case strings
dracula_text = readBook().lower().split()

print("=== Results ===")
print("")

# Create book dictionary with unique words and their word count
dracula_dictionary = get_dictionary(dracula_text)

# The word that shows up the most often
most_common_word = get_most_common_word(dracula_dictionary)
print(f"'{most_common_word}' is the word that appears the most throughout the text a total of {dracula_dictionary[most_common_word]} times")
print("")

# Four-letter words that are in the book
four_letter_word_cnt = get_four_letter_word_cnt(dracula_dictionary)
print(f"There are {four_letter_word_cnt} words that are four letters long")
print("")

# Every word that shows up at least five hundred times
word_dict_500 = get_words_500(dracula_dictionary)
print(f"I noticed that these words show up 500 or more times:")
for word in word_dict_500:
  print(f"{word} - {word_dict_500[word]}")
