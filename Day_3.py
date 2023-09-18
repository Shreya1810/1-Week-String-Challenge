def palindrome_check(string):
  string = string.lower().replace(' ','')
  
  return string == string[::-1]


string = input("Enter a string: ")
print(palindrome_check(string))