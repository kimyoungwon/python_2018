# Name: Youngwon Kim
# CSE 160
# Homework 2: DNA analysis

# This program reads in DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
#
# For teaching purposes, a few more comments than normal have been added in
# to explain in detail what some Python constructs are doing.

# The sys module supports reading files, command-line arguments, etc.
import sys

# Function to convert the contents of dna_filename into a string of nucleotides
def filename_to_string(dna_filename):
    """ 
    dna_filename - the name of a file in expected file format 
    Expected file format is: Starting with the second line of the file, 
    every fourth line contains nucleotides.  
    The function will read in all lines from the file containing nucleotides, 
    concatenate them all into a single string, and return that string.
    """

    # YOU DO NOT NEED TO MODIFY THIS FUNCTION.

    # Creates a file object from which data can be read.
    inputfile = open(dna_filename)

    # String containing all nucleotides that have been read from the file so far.
    seq = ""

    # The current line number (= the number of lines read so far).
    linenum = 0

    for line in inputfile:
        linenum = linenum + 1
        # if we are on the 2nd, 6th, 10th line...
        if linenum % 4 == 2:
            # Remove the newline characters from the end of the line
            line = line.rstrip()
            # Concatenate this line to the end of the current string
            seq = seq + line
    return seq
    
# Function to return GC Classification
def classify(gc_content):
    classification = gc_content
    if gc_content > .6:
        return 'high'
    elif gc_content > .4:
        return 'moderate'
    elif gc_content > .2:
        return 'low'
    return classification

###########################################################################
### Main program begins here
###

# Check if the user provided an argument
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)

# Save the 1st argument provided by the user, as a string.
# Note: sys.argv[0] is the name of the program itself (dna_analysis.py)
filename = sys.argv[1]

# Open the file and read in all nucleotides into a single string of letters
nucleotides = filename_to_string(filename)

###
### Compute statistics
###

# YOUR CODE GOES BELOW THIS POINT

# Number of G and C nucleotides seen so far and number of A and T nucleotides seen so far.

gc_count = 0
at_count = 0

for base in nucleotides:
    
    if base == 'C' or base == 'G':
        gc_count = gc_count + 1
    elif base == 'A' or base == 'T':
        at_count = at_count + 1
  
# Number of G,C,A and T/G and C/A and T nucleotides seen so far.
total_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0

for base in nucleotides:
    total_count = total_count + 1

    if base == 'G':
        g_count = g_count + 1
    elif base == 'C':
        c_count = c_count + 1
    elif base == 'A':
        a_count = a_count + 1
    elif base == 'T':
        t_count = t_count + 1

sum_contents = g_count + c_count + a_count + t_count
gc_content = float(gc_count) / sum_contents
at_content = float(at_count) / sum_contents

print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G-count:', g_count
print 'C-count:', c_count
print 'A-count:', a_count
print 'T-count:', t_count
print 'Sum of G+C+A+T:', sum_contents
print 'Total count:', total_count
print 'Length of nucleotides:', len(nucleotides)

g_count = float(g_count) 
c_count = float(c_count)
a_count = float(a_count)
t_conut = float(t_count) 

print "AT/GC Ratio:", (a_count+t_count)/(g_count + c_count)
print "GC Classification:", classify(gc_content)

# You can add more assertions here to check properties that you think
# should be true about your results. If the condition listed is false,
# then the given message will be printed.
assert total_count == len(nucleotides), "total_count != length of nucleotides"
