#!/usr/bin/python3


def inverse(x = ''):
	"function that calculates the inversion of a chain"
	try:
		output = ""
		for c in x:
			output = c + output
		return output
	except:
		return "Ups...There has been some problem!"


print("The inverse of 'Hello' is: ", inverse('Hello'))
print("The inverse of '123' is: ", inverse('123'))
print("The inverse of a number is: ", inverse(123))
print("The inverse of an empty string is: ", inverse(''))
print("The inverse of nothing is: ", inverse())
print("The inverse of an array is: ", inverse([1 , 'Hello']))
