n = 100
b = 1
a = 0
x = 0
y = 0
series = 'sum'

if series == 'fibonacci':
    for i in range (n):
     a, b= b, a+b
    print a
elif series == "sum":
    for i in range (n):
     y += (3 * i)
     x = y + (3*n)
    print x
else: 
 print "Invalid string."




