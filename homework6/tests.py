# CSE 160
# Tests for Homework 6: Detecting Fraudulent Data
# UW NetID: 1724787
# CSE 160

import fraud_detection
reload(fraud_detection)
from fraud_detection import *

## Comparison functions that don't compare floats using '=='
## Duplicates this part from homework 5's tests.py

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

def test_extract_election_vote_counts(): 
    assert eq(extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]), [1131111, 16920, 7246, 837858, 623946, 12199, 21609, 656508, 325911, 6578, 2319, 302825, 1799255, 51788, 14579, 746697, 199654, 5221, 7471, 96826, 299357, 7608, 3563, 177268, 3819495, 147487, 67334, 3371523, 359578, 22689, 4127, 106099, 285984, 3962, 928, 90363, 2214801, 44809, 13561, 884570, 341104, 4129, 2478, 113218, 1303129, 139124, 15934, 552636, 444480, 7276, 2223, 126561, 295177, 4440, 2147, 77754, 450269, 6616, 12504, 507946, 1758026, 23871, 16277, 706764, 498061, 7978, 2690, 177542, 422457, 16297, 2314, 148467, 315689, 7140, 13862, 261772, 1160446, 12016, 4977, 318250, 573568, 11258, 10798, 374188, 253962, 8542, 4274, 98937, 515211, 5987, 10097, 325806, 998573, 12022, 7183, 453806, 677829, 14920, 44036, 219156, 1289257, 19587, 10050, 585373, 572988, 10057, 4675, 190349, 482990, 7237, 5126, 241988, 765723, 13117, 12032, 218481, 337178, 8406, 2565, 255799])

def test_ones_and_tens_digit_histogram():
    assert eq(ones_and_tens_digit_histogram([0]), [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    assert eq(ones_and_tens_digit_histogram([10]), [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    assert eq(ones_and_tens_digit_histogram([127, 426, 28, 9, 90]), [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2])
    assert eq(ones_and_tens_digit_histogram([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]),[0.21428571428571427, 0.14285714285714285, 0.047619047619047616, 0.11904761904761904, 0.09523809523809523, 0.09523809523809523, 0.023809523809523808, 0.09523809523809523, 0.11904761904761904, 0.047619047619047616])

def test_plot_iranian_least_digits_histogram():
    # No tests provided for the plot_iranian_least_digits_histogram function
    pass

def test_random_group():   
    # No tests provided for the random_group function
    pass

def test_plot_distribution_by_sample_size():
    # No tests provided for the plot_distribution_by_sample_size function
    pass

def test_mean_squared_error():
    assert eq(mean_squared_error([1, 2, 3], [1, 2, 3]),0)   
    assert eq(mean_squared_error([2, 4, 6], [2, 4, 6]),0)
    assert eq(mean_squared_error([1, 4, 9], [6, 5, 4]),17)

def test_calculate_mse_with_uniform():
    assert eq(calculate_mse_with_uniform(ones_and_tens_digit_histogram(extract_election_vote_counts("election-iran-2009.csv",["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]))), 0.000739583333333)
        
def test_compare_mse_to_samples():
    # No tests provided for the compare_mse_to_samples function
    pass

def test_compare_iranian_mse_to_samples():
    # No tests provided for the compare_iranian_mse_to_samples function
    pass

def test_compare_us_mse_to_samples():
    # No tests provided for the compare_us_mse_to_samples function
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
    test_extract_election_vote_counts()
    test_ones_and_tens_digit_histogram()
    test_plot_iranian_least_digits_histogram()
    test_plot_iranian_least_digits_histogram()
    test_random_group()
    test_plot_distribution_by_sample_size()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()
    test_compare_mse_to_samples()
    test_compare_iranian_mse_to_samples()
    test_compare_us_mse_to_samples()
    print "Tests passed."
