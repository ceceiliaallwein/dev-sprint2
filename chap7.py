# Enter your answrs for chapter 7 here
# Name:


# Ex. 7.5

import math 

def factorial(k): 
	if k == 0: 
		return 1 
	else: 
		loop = 

def estimate_pi(k):
	'''Uses the infinite series 
	of Srinivasa Ramanujan to 
	compute a value of pi with 
	a given value for k. 

	n = number of iterations
	k = given value of k 
	e = epsilon
	lh = expression for pi; left hand side of series
	r = quotient  
	s = sum   
	rh = right hand side of the equation
	'''
	n = 0
	k = 0 
	e = 1e-15	
	left_hand = 1/math.pi
	coefficient = 2*math.sqrt(2)/9801
	numerator = math.factorial(4*k)*(1103+26390*k)
	denominator = (math.factorial(k))**4)*(396**(4*k)))
	right_hand = coefficient * (numerator/denominator)

	while True: 
		
		# ensures that k is not a negative number 
		if k <0:
			print "Please try again. Function \
			defined for positive integers only."
			return k
			
		else: 
			result = 
			right_hand = 

		k += 1
		n += 1







# How many iterations does it take to converge?


		