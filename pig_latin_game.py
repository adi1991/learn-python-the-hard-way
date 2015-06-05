#import enchant
#import re

#print "Welcome to the pig latin game"

#match = enchant.Dict("en_US")

#while True:
#	word = str(raw_input("Please enter a valid word: "))
#	if match.check(word) and re.match('[a-z]+$',word):	
#		first = word.replace(word[1:], '')
#		whole = word.replace(word[:1], '')
#		new_word = whole + first + "ay"

#		print "The new word is", new_word
		
#	else:
#		print "The word is not valid"


import enchant

print "welcome to the pygLatin game"

while True:
	match = enchant.Dict("en_US")

	user_input_word = raw_input("Please enter a valid number: ")

	if len(user_input_word) > 0 and user_input_word.isalpha() and 			match.check		(user_input_word):
		pyg = 'ay'
		first = user_input_word[0]
	
		new_word = user_input_word + first + pyg 
		new_word = new_word[1:]	
		print new_word
	else:	
		print "The word is not valid"
	
