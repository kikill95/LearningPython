# Declart a variable and initialize it
f = 0;
print f

# re-declaring the variable works
f = 'abc'
print f

# Error: Different types cannot be combined
#print "string type" + 123
print "string type " + str(123)

# Global vs. local variables in functions
def main():
	# global f
	f = 'hello'
	print f

main()
print f # Local variale f = abc

# Global vs. local variables in functions
def main():
	global f
	f = 'hello'
	print f

main()
print f # f - is a global varible

del f # Delete variable f
print f # Get error: "NameError: global name 'f' is not defined"