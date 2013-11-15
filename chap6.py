# Enter your answers for chapter 6 here
# Name: Ceceilia Allwein



#############
## Ex. 6.1 ##
#############


def compare(x,y):
	'''
	Compares two integers and returns the larger one. 
	If both are equal, it returns zero.
	If no conditions are met, it returns the first number. 
	'''
	if x > y:
#		print x,'is larger than', y
		return x
	elif x < y:
#		print y,'is larger than',x
		return y
	elif x == y: 
#		print x,'and',y,'are equal.'
		return x-y
	else:
#		print 'Try again. No conditions met.'
		return x

compare(2,3)



#############
## Ex. 6.2 ##
#############


import math


def hypotenuse(x,y):
	'''
	Calculates the hypotenuse of a triangle with given 
	sides x and y using the Pythagorean Theorem. 

	Scaffolding includes the variable check, which 
	verifies that both sides of the equation balance. 

	Returns float 
	'''
	x_sq = x**2
	y_sq = y**2
	sum_sq = x_sq + y_sq
	result = math.sqrt(sum_sq)
#	check = int(result**2-sum_sq)
#	print x,'squared is', x_sq
#	print y,'squared is', y_sq
#	print 'Sum squared is:', sum_sq
#	print result
#	print check
	return result

hypotenuse(2,3)



#############
## Ex. 6.3 ##
#############


def is_between(x,y,z): 
	'''
	Determines whether three given numbers
	are sequential and / or equal. 

	Returns a boolean.  
	'''
	if x <= y <= z: 
		return True
	else: 
		return False

is_between(5,7,1)



##########################
## Ex. 6.6 (palindrome) ##
##########################


def first(word):
	'''
	Returns the first letter in a string.
	'''
	return word[0]


def last(word):
	'''
	Returns the last letter in a string.
	'''
	return word[-1]


def middle(word):
	'''
	Returns a given string w/o the 
	first and last letters. 
	'''
	return word[1:-1]


def start_palindrome(word):
	return first(word) == last(word)


def is_palidrome(word):
	'''
	Determines if a word is a palindrome by 
	comparing first and last letters, then 
	extracting the middle. 

	It recurses, until the number of elements
	in the string reaches zero. 
	'''
	num_it = 0
	while len(word) > 0: 
		if start_palindrome(word): 
			word = middle(word)  
#			print num_it
#			print word 
			num_it += 1
		else: 
#			print False
			return False 

                                
is_palidrome('rotator')



#####################
## Ex. 6.7 (power) ##
#####################


def is_divisible(a,b):
	return a % b == 0


def is_power (a,b):
	temp = a/b 
	if is_divisible(a,b):
		result = is_power(temp,b)
#		print result
		return result
	else:
#		print False
		return False

is_divisible(2,3)



###################
## Ex. 6.8 (GCD) ##
###################

def gcd(a,b):
	'''
	Calculates the greatest common divisor (GCD) of two 
	given numbers.

	Runs automatically via the main constructor.

	a = int
	b = int 
	'''
	if b == 0: 
		return a
	if a == 0:
		return b
	'''puts larger number in the numerator'''
	if a < b: 		
		temp = b
		b = a
		a = temp 
	'''r is by definition always + or 0 '''
	r = a % b
	if r > 0:
		gcd (b,r)
		return r
	'''Runs when r=0'''
	else:  
#		print b
		return b


def print_gcd(a,b):
	'''Separates display from logic of the gcd function'''
	print 'The GCD of',a,'and',b, 'is', gcd(a,b)


def main(args):
	'''Defines main function and converts user input
	to integers, per gcd function parameters.'''
 	print_gcd( int(args[0]), int(args[1]) )


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])













