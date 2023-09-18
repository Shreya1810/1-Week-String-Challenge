def reverse_str(my_string):
  rev = ''
  for i in my_string:
    rev = i + rev 

  return rev
  



my_string = input("enter a string: ")
print(reverse_str(my_string))
