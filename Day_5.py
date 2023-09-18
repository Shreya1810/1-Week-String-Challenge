'''Create a function that takes a sentence as input and capitalizes the first letter of each word'''

def capitalize_sentence(sentence):
  words = sentence.split(' ')
  new = ' '
  for word in words:
    new = new +  word.capitalize() + " "

  return new
  
sentence = input("Enter a sentence: ") 
print(capitalize_sentence(sentence))
   