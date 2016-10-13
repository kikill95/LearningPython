class myClass():
	def method1(self): # usually the first argument of method in the class = sel
		print 'myClass method1'

	def method2(self, someString):
		print 'myClass method2: ' + someString

class anotherClass(myClass): # anotherClass is based on myClass
	def method2(self): # this methor override method2 in myClass
		print 'anotherClass method2'

	def method1(self):
		myClass.method1(self);
		print 'anotherClass method1'

def main():
	c = myClass()
	c.method1()
	c.method2('This is a string')

	c2 = anotherClass()
	c2.method1()
	c2.method2()

if __name__ == "__main__":
	main()