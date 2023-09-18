def count_vowels(my_string):
  count = 0
  vowels = ['a', 'e', 'i', 'o', 'u']

  for char in my_string.lower():
    if char in vowels:
      count += 1
      
  return f"Number of vowels in the given string : {count}"

my_string = input("Enter a string: ")
print(count_vowels(my_string))