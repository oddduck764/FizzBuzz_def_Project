
import sys

number = raw_input("Enter any number silly:  ")
number = int(number)

def Dby2(x):
	if number % 2 == 0:
		print "True"
	else:
		print "False"

def FizzBuzz(n):
	if number % 15 == 0:
		print "FizzBuzz"

	elif number % 3 == 0:
		print "Fizz"
	
	elif number % 5 == 0:
		print "Buzz"
	
	else:
		print (number)


Dby2(number)

FizzBuzz(number)
