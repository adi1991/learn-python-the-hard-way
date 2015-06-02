from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print "copying from %s to %s" %(fromFile, toFile)

inFile = open(fromFile)
inData = inFile.read()

print "The input data is %d bytes long" % len(inData)

print "Does the output file exsist? %r" % exists(toFile)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

outFile = open(toFile, 'w')
outFile.write(inData)

print "Alright, all done"

outFile.close()
inFile.close()
  
