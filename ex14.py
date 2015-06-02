#ex14
from sys import argv

script, your_name = argv
prompt = '> '

print "Hi %s, I'm the %s script."% (your_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % your_name
like = raw_input(prompt)
print "Where do you live %s?" % your_name
lives = raw_input(prompt)
print "What kind of computer do you have %s?"
computer = raw_input(prompt)

print """
Alright, So you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer, Nice.
"""%(like, lives, computer)






## extra
#from sys import argv

#script, your_name = argv
#prompt = '> '

#print "Hi %s, I'm the %s script ghost."% (your_name, script)
#print "I have come down here to scare you. I have three questions to ask if you answer them correctly I will let you go."
#print "first question. What is the average span life of a Human being"
#years = raw_input(prompt) 
#print "Second question. What is your favourite pass time?"
#time = raw_input(prompt)
#print "Third queston. What is the name of my cat that the pharos used to pray to?"
#cat = raw_input(prompt)
#print "Alright, So %s I am happy with your answers now do you have any questions to ask me?"% (your_name)
#question = raw_input(prompt)
#answer = raw_input(prompt)
#print "goodbye %s. Hope to see you on the other side."% (your_name)
#bye = raw_input(prompt)

