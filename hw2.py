# Name: Robin Bartels
# Evergreen Login: Barrob16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test
from hw2_test import n
n = 100

while ( n < 5050):
    n = (n - n) + n + 1
print (n)



# When I try to import n from hw2_test, it keeps giving the integer "1", no matter
# what I do. I manually had to set n to 100 






###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE

print "Problem 2 solution follows:"

for i in range (2, 11):
    print 1.0/i

# This problem and figuring out a very short for loop, took hours.

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0

for i in range (n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
for i in range (1, n):
     n = n * i
print (n)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10

for i in range (1, numlines + 1 ):
    n = (numlines + 1) - i
    for i in range (1, n):
        n = n * i
    print (n)



###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"


for i in range (2, 11):
    n = 1.0/i
    for i in range (1, n):
        n = (n + 1) * i
print (n)

###
### Collaboration
###

# Mary...

###
### Reflection
###


# Used stack overflow.com a very helpful python debugging website, and many other websites--
# Khan academy, various google searches for using loops


# It took between 3-4 hours, or maybe 5 to complete this assignment. 
# I don't feel I was adequately prepared with readings/lecturs to complete this. 
# I know confusion is a important concept in this class, but I believe there is a balance
# And to me it feels like I am too confused for it to be helpful, with just a little bit more focused instruction
# It would become healthy confusion for me, rather then unhealthy confusion.
# Having you go over for loops on monday would have been greatly helpful.

