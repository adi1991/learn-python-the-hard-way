def print_two(*args):
	args1, args2 = args
	print "arg1: %r, args: %r" %(args1, args2)

def print_two_again(args1, args2):
	print "arg1: %r, arg2: %r" %(args1, args2)

def print_one(args1):
	print "arg1: %r" % args1

def print_none():
	print "I got nothing"

print_two("Aditya", "Seshan")
print_two_again("Aditya", "Seshan")
print_one("First!")
print_none()
