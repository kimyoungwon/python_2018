# CSE 160
# Tests for Homework 7: Final Project
# UW NetID: 1724787
# CSE 160

import schoolreadiness
reload(schoolreadiness)
from schoolreadiness import *

## Comparison functions that don't compare floats using '=='
## Duplicates this part from homework 5 and 6's tests.py

def eq(e, a):
    # == is stricter than this function, so if e == a is true,
    # then eq(e, a) would be true as well.  
    if e == a:
        return True

    # Compare ints as float instead
    if type(e) == int:
        e = float(e)
    if type(a) == int:
        a = float(a)

    # Arguments must be of the same type.
    if type(e) != type(a):
        return False

    # Delegate to a more specific comparator. Only the types
    # for this assignment are implemented.
    if type(e) == dict:
        return eq_dict(e, a)
    elif type(e) == float:
        return eq_float(e, a)
    elif type(e) == str:
        return eq_str(e, a)

def eq_dict(e, a):
    # In this assignment, keys will never be float, so this 
    # comparison is okay.
    if sorted(e.keys()) != sorted(a.keys()):
        return False

    for key in e:
      if not eq(e[key], a[key]):
          return False

    return True

def eq_float(e, a):
    """Returns true of e is within 0.00001 of a.
    
    Take-away point: You should never compare floats using ==
    
    Explanation:
    Computers store floating point numbers as only an approximation
    of the actual value.  This is not just a limitation of Python, it is
    true in most languages and is due to the way floating point numbers
    are stored as bits in computers. See ICPUP section 3.4 for more info.
    Try typing this example into the Python interpreter (adding 0.1 ten times):
    >>> b = .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1 + .1
    >>> b
    0.9999999999999999
    >>> b == 1.0
    False
    Since 0.1 cannot be represented exactly in floating point, adding 
    together 0.1 ten times does NOT equal 1.0 exactly!! It is not just 
    this example, it happens for many values and combining (or taking
    the difference, or dividing, etc.) these inexact values will 
    accumulate and amplify minor differences as you manipulate a 
    floating point value multiple times.
 
    So instead of testing for equality, whenever you want to check to see
    if two floating point values are equal, you should use a technique 
    like we do here: you should check if value e is *within some epsilon* 
    of value a. We can pick epsilon to be however small/close we want.
    In this case we arbitrarily picked 0.00001 as "close enough to be 
    considered equal".  
    """
    epsilon = 0.00001
    return abs(e - a) < epsilon

def eq_str(e, a):
    return e == a

## The tests

def test_read_csv():
    # No tests provided for the read_csv function
    pass

example_set = [{'self_efficacy_1':'2','grit_1':'1','grit_2':'3'}, \
               {'self_efficacy_1':'3','grit_1':'2','grit_2':'4'}, \
               {'self_efficacy_1':'4','grit_1':'3','grit_2':'7'}]

def test_number_of_variables(): 
    assert eq(number_of_variables(example_set,"self_efficacy"), 1)
    assert eq(number_of_variables(example_set,"grit"), 2)

def test_means_of_variables():
    assert eq(means_of_variables(example_set,"self_efficacy"),[2,3,4])    
    assert eq(means_of_variables(example_set,"grit"),[2,3,5])         

def test_make_a_new_dict():
    assert eq(make_a_new_dict(example_set,["self_efficacy"]),{'self_efficacy':[2.0,3.0,4.0]})    
    assert eq(make_a_new_dict(example_set,["grit"]),{'grit': [2.0, 3.0, 5.0]})         

example_dic = {'gender':[1,1,2]}

def test_count_gender():
    assert eq(count_gender(example_dic,"gender"),(2,1))    
    
def test_get_pearsonr():
    # No tests provided for the get_pearsonr function
    pass

def test_bar_grapgh():
    # No tests provided for the bar_grapgh function
    pass

def test_scatter_plot():
    # No tests provided for the scatter_plot function
    pass


# If this file, tests.py, is run as a Python script (such as by typing
# "python tests.py" at the command shell), then run the following tests:
if __name__ == "__main__":
    # TODO: Uncomment these function calls as you complete each part, to test
    # your implementation:

    print "**************************************"
    print "**** You are running tests.py ********"
    print "**************************************"
    test_read_csv()
    test_number_of_variables()
    test_means_of_variables()
    test_make_a_new_dict()
    test_count_gender()
    test_get_pearsonr()
    test_bar_grapgh()
    test_scatter_plot()
    print "Tests passed."
