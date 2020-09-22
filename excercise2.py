#!/usr/bin/python3

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def isVowel(x):
	"function that takes a character and returns True if it is a vowel, otherwise it returns False"
	try:
		if x.isalpha() and x in vowels: return True
		return False
	except:
		return False


print("isVowel('a'): ", isVowel('a'))
print("isVowel('x'): ", isVowel('x'))
# print("isVowel(): ", isVowel())
print("isVowel(3): ", isVowel(3))
print("isVowel('.'): ", isVowel('.'))
print("isVowel('_'): ", isVowel('_'))
print("isVowel('3'): ", isVowel('3'))
print("isVowel(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')): ", isVowel(vowels))

