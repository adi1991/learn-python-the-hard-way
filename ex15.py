#ex15
from sys import argv

script, filename = argv

txt = open(filename)
print "Here is your first file %r" % filename
print txt.read()

print "Print the file again:"
file_again = raw_input(" >")


txt_again = open(file_again)
print txt_again.read()








#
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

