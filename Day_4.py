'''Create a function that removes all duplicate characters from a string,preserving the order of the remaining characters.
'''

my_string = input("Enter a string: ")

def remove_duplicates(my_string):
  k = []
  for i in my_string:
    if i not in k:
      k.append(i)
      
  return ''.join(k)

print(remove_duplicates(my_string))