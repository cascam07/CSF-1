# Name: Robin Bartels
# Evergreen Login: Barrob16
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""     
# The current line number (= the number of lines read so far).
linenum = 0 


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0

# Individual A, T, G, C Nucleotides present.
A_nucleotides = 0
T_nucleotides = 0
G_nucleotides = 0
C_nucleotides = 0

# Total A, T, G, C nucleotides
sum_count = 0
x = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1
    
    # next, if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1
        
    if bp == 'C' or bp == 'G':
       gc_count = gc_count + 1

    if bp == 'A':
        A_nucleotides = A_nucleotides + 1

    if bp == 'T':
        T_nucleotides = T_nucleotides + 1

    if bp == 'G':
        G_nucleotides = G_nucleotides + 1
    
    if bp == 'C':  
        C_nucleotides = C_nucleotides + 1  


# Computes AT/GC Ratio
ATGC_Ratio = float(at_count) / gc_count

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count

# The GC content can be used to categorize microorganisms.
if float(gc_content) > .60:
    x = 'high GC content'
if float(gc_content) < .40:
    x = 'low GC content'
if float(gc_content) < .60 and float(gc_content) > .40:
    x = 'moderate GC content'


# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G nucleotides:', G_nucleotides
print 'C nucleotides:', C_nucleotides
print 'A nucleotides:', A_nucleotides
print 'T nucleotides:', T_nucleotides
print 'Sum count:', G_nucleotides + C_nucleotides + A_nucleotides + T_nucleotides
print 'Total count:', total_count
print 'seq length:', len(seq)
print 'AT/GC Ratio:', float(ATGC_Ratio)
print 'GC Classification:', x

#Riley McGavik conceptulizing DNA, Nucleotides/understanding base pairs/BP's