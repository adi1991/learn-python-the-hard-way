import enchant
import re

print "Welcome to the pig latin game"

match = enchant.Dict("en_US")

while True:
	word = str(raw_input("Please enter a valid word: "))
	if match.check(word) and re.match('[a-z]+$',word):	
		first = word.replace(word[1:], '')
		whole = word.replace(word[:1], '')
		new_word = whole + first + "ay"

		print "The new word is", new_word
		
	else:
		print "The word is not valid"
