print("_____________________________________")
print("Welcome User")
print("Tool Name: WRDLST-GENERATOR")
print("Purpose: Wordlist creation")
print("Licence: WTFPL Licence")
print("-------------------------------------")
print("Give Datails, I mean words about the Targeted Victims. How much details u give that much possibility of success. Scientifically How much words you give that was close to the target is driectly propotional to the success rate. ")
print("-------------------------------------")

# Import the necessary modules
import itertools

# Set the minimum and maximum length of the words in the wordlist
min_length = 1
max_length = 6

# Ask the user to provide a list of words
words = input('Enter a list of words: ').split()

# Open a file for writing the wordlist
with open('wordlist.txt', 'w') as f:
  # Use the itertools module to generate all possible combinations of words
  # with the specified length range
  for length in range(min_length, max_length + 1):
    for word in itertools.combinations_with_replacement(words, length):
      # Write each generated word to the file
      f.write(''.join(word) + '\n')

