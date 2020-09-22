#!/usr/bin/python3


def countChars(x = ''):
	"Given a string, count all the characters occurrences"
	try:
		register = {}
		for c in x:
			if c in register: 
			    register[c] = register[c] + 1
			else:
			    register[c] = 1
		return register
	except:
		return "Ups...There has been some problem!"

print("The counting result for 'Hello' is: ", countChars('Hello'))
print("The counting result for '111123' is: ", countChars('111123'))
print("The counting result for nothing is: ", countChars())
print("The counting result for 123 is: ", countChars(123))
