# Name: Youngwon Kim
# CSE 160
# Spring 2018
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and then copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all of the problems given.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 3
b = 5.86
c = 2.5408
d = b**2-4*a*c

if d<0:
        print "no answer!"
elif d == 0:
    x = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    print "Answer:", x
    
else:
    x1 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    print "Answer:", x1, "and", x2

###
### Problem 2
###

print "Problem 2 solution follows:"

for num in range(2,10):
    decimal = 1./num
    print "The decimal of", "1 /", num, "is", decimal 

###
### Problem 3
###

print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(1,n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n * (n + 1) / 2

###
### Problem 4
###

print "Problem 4 solution follows:"

n = 10
factorial = 1

for n in range(1,n+1):
    factorial = factorial * n 
print "The answer of " + str(n) + "!" +  " is " + str(factorial)


###
### Problem 5
###

print "Problem 5 solution follows:"

numlines = 10
for m in range(numlines, 0, -1):
    factorial = 1
    for l in range(1, m+1):
        factorial = factorial * l
    print str(m) + "!" +  " : " + str(factorial)

###
### Problem 6
###

print "Problem 6 solution follows:"

num = 10
for p in [10]:
    factorial = 1
    factorial2 =0
    for q in range(1, p+1):
        factorial = factorial * q
        factorial2 = factorial2 + 1./factorial
print "The sum of 1 + 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/10! is " + str(1+factorial2)


###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").


