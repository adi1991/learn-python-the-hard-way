def censor(text, word):
	censor = ""	
		#print i
	if word in text:
			#print i
		ast = len(word) 
		censor = text.replace(word, '*'*ast)
			
	print censor
	return censor

censor ('hello hey hey How are you?', "hey")

