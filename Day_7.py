'''Write a function that finds the longest word in a sentence and returns it.'''

def longest_word(sentence):
  words = sentence.split(' ')
  max_len = 0
  for word in words:
    len_word = len(word)
    if len_word > max_len:
      max_len = len_word

  if max_len == len(word):
    return f"The longest word in this sentence is '{word}' with a length of {max_len}"




sentence = input("Enter a sentence: ")
print(longest_word(sentence))