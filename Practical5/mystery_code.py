# What does this piece of code do?
# Answer: print a random number in 1-49
# Take a random number in 1-100. If it is greater than 50, fetch the number again until it reaches a number less than 50. Then print the number

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)
