from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second  variable is:", second
print "Your third variable is:", third


#ex14
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

#ex15
#from sys import argv

#script, your_name, filename1, filename2, filename3 = argv

#prompt = '> '
#txt1 = open(filename1)
#print "Hi %s, We have three files for you. Please see the first file %r" % (your_name, filename1)
#print txt1.read()
#print "%s can you guess the name of song and which movie it come is?"% your_name
#ans1 = raw_input(prompt)

#txt2 = open(filename2)
#print "now open the second file %r"% filename2
#print txt2.read()
#print "can you find the final answer to this"
#ans2 = raw_input(prompt)

#txt3 = open(filename3)
#print "now open the third file %r"% filename3
#print txt3.read()
#print "enjoy and have a nice day"

#ex16
#from sys import argv

#script, filename = argv

#print "we're going to erase %r."% filename
#print "If your don't want that, hit CTRL-C(^C)"
#print "If you do want that, hit RETURN."

#raw_input("?")

#print "opening the file..."
#target = open(filename, 'w')

#print "Truncating the file. Goodbye!"
#target.truncate()

#print "Now I'm going to ask you for three lines."

#line1 = raw_input("line 1: ")
#line2 = raw_input("line 2: ")
#line3 = raw_input("line 3: ")
#line4 = raw_input("line 4: ")
#line5 = raw_input("line 5: ")
#line6 = raw_input("line 6: ")

#print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#target.write(line4)
#target.write("\n")
#target.write(line5)
#target.write("\n")
#target.write(line6)
#target.write("\n")

#print "And finally, we close it."
#target.close()




# learn-python-the-hard-way ex3.py ex4.py ex5.py ex6.py ex7.py ex8.py ex9.py ex10.py ex11.py ex12.py ex13.py ex14.py ex15.py ex16.py ex17.py ex18.py ex19.py
