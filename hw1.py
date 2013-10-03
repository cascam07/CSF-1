# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

import math
from math import sqrt

a = 1

b = 5.86

c = 8.5408

x = (-b + sqrt(b**2 - 4*(a*c)))/2*a

y = (-b - sqrt(b**2 - 4*(a*c)))/2*a

print x
print y

# Had trouble with syntax error at first. It is still computing wrong answer, don't know how to fix.
# Read the chapters in Python book- realized b** does not equal b^2. Rather it is B**2

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test

from hw1_test import a, b, c, d, e, f

print str (a), str (b), str (c), str (d), str (e), str (f)


###
### Problem 3
###


print "Problem 3 solution follows:"


a = True
b = False
c = True
d = False
e = False
f = True

x= ((a and b) or (not c) and not (d or e or f))

print x

###
### Collaboration
###

# Got help from another student in library on equation for Prob# 1, don't know her name though.
# Took me around 1-2 hours...mainly the first problem and working out syntax errors. Did not realize there was a tutorial
# Pretty ignorant of me, it would have saved me some time I think in looking at them beforehand.
