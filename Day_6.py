#Create a function that replaces all spaces in a string with hyphens("-")

def replace_spaces(string):
  return string.replace(' ','-')


string = input("Enter a string : ")
print(replace_spaces(string))