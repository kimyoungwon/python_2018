# Name: Youngwon Kim
# UW NetID: 1724787
# CSE 160
# Homework 6: Detecting Fraudulent Data

import csv
import random
import matplotlib.pyplot as plt

################################################################################
# Problem 1: Read and clean Iranian election data
################################################################################

def read_csv(path):
    """Reads the CSV file at path, and returns a list of rows from the file.

    Parameters:
        path: a path to a CSV file. 
        
    Returns:
        list of dictionaries: Each dictionary maps the columns of the CSV file
        to the values found in one row of the CSV file.
    """
    data = []
    csv_file = open(path)
    for row in csv.DictReader(csv_file):
        data.append(row)
    csv_file.close()    
    return data

def extract_election_vote_counts(filename, column_names):
    """Given a list of dictionaries from 'filename', returns a list of integers 
       in 'column_names'

    Parameters:
        filename: a path to a CSV file. 
        column_names: a list of column names
        
    Returns:
        list of integers: The values in 'column_names' can be found in every row 
        of a list of dictionaires. The order of the integers does not matter.
    """
    
    open_file = read_csv(filename)
    vote_counts = []
    for row in open_file:
        for key in column_names:
            if row[key] != "":
                vote_counts.append(int(row[key].replace(',', '')))
    return vote_counts

################################################################################
# Problem 2: Make a histogram
################################################################################

def ones_and_tens_digit_histogram(numbers):
    """Given a list of numbers, returns a list of 10 numbers.

    Parameters:
        numbers: a list of numbers
        
    Returns:
        list of numbers: The value at index i is the frequency with which digit i 
        appeared in the ones place OR the tens place in the input list.
    """
    ones_or_tens_digit = [0,0,0,0,0,0,0,0,0,0]
    total_number_of_digits = 0
    for i in numbers:
        ones_digit = 0
        tens_digit = 0    
        total_number_of_digits += 1
        if 100 < i :
            tens_digit = (i/10) % 10
            ones_digit = i%10
        elif i < 100:
            tens_digit = i/10
            ones_digit = i%10
        ones_or_tens_digit[ones_digit] += 1
        ones_or_tens_digit[tens_digit] += 1
        
    ones_or_tens = []
    for i in ones_or_tens_digit:
        ones_or_tens.append(i / float(2*total_number_of_digits))
        
    return ones_or_tens

################################################################################
# Problem 3: Plot election data
################################################################################        

def plot_iranian_least_digits_histogram(histogram):
    """Given a histogram, graphs the frequencies of the ones and tens digits for 
       the Iranian election data

    Parameters:
        histogram: list of the frequencies created by *ones_and_tens_digit_histogram*.

    Returns:
        None
    """
    plt.clf() # Deletes the previous plot
    plt.plot([0.10] * 10, color = 'blue', label = 'Ideal')
    plt.plot(histogram, color = 'orange', label = 'Iran')
    plt.legend()
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.savefig("iran-digits.png")
    #plt.show()


################################################################################
# Problem 4: Smaller samples have more variation
################################################################################        

def random_group(number_of_group):
    """Creates a list of a group with random numbers from 0 to 99.

    Parameters:
        number_of_group: a number of group (or size)

    Returns:
        list of a group: a group cosists of random numbers from 0 to 99.
    """    
    group = []
    for i in range(number_of_group):
        group.append(random.randint(0, 99))
    return group

def plot_distribution_by_sample_size():
    """Creates five different collections (size 10, 50, 100, 1000, and 10,000) 
       of random numbers where every element in the collection is a different 
       random number x such that 0 <= x < 100.

    Parameters:
        None

    Returns:
        None
    """
    first_group = ones_and_tens_digit_histogram(random_group(10))
    second_group = ones_and_tens_digit_histogram(random_group(50))
    third_group = ones_and_tens_digit_histogram(random_group(100))
    fourth_group = ones_and_tens_digit_histogram(random_group(1000))
    fifth_group = ones_and_tens_digit_histogram(random_group(10000))
    
    plt.clf() # Deletes the previous plot
    plt.axis([0, 9, 0, 0.25])
    plt.title('Distribution of last two digits')
    plt.plot([0.10] * 10, color = 'blue', label = 'Ideal')
    plt.plot(first_group, color = 'cyan', label = '10 random numbers')
    plt.plot(second_group, color = 'green', label = '50 random numbers')
    plt.plot(third_group, color = 'purple', label = '100 random numbers')
    plt.plot(fourth_group, color = 'yellow', label = '1000 random numbers')
    plt.plot(fifth_group, color = 'red', label = '10000 random numbers')
    plt.legend()
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.savefig("random-digits.png")
    #plt.show()

################################################################################
# Problem 5: Comparing variation of samples
################################################################################        

def mean_squared_error(numbers1, numbers2):
    """Takes two lists of numbers and returns the mean squared error (MSE) 
       between the lists.

    Parameters:
        numbers1: a list of numbers1.
        numbers2: a list of numbers2.

    Returns:
        MSE between the lists: The larger the value of MSE is, the more different 
        the two lists (graphs) are. (0: the two lists are same.)
    """
    squared_error = 0
    for num in range(len(numbers1)):
        squared_error += (numbers1[num] - numbers2[num]) ** 2
    MSE = squared_error / len(numbers1)   

    return MSE

################################################################################
# Problem 6: Comparing variation of samples
################################################################################        

def calculate_mse_with_uniform(histogram):
    """Given a histogram, returns the mean squared error (MSE)
       between the histogram and the uniform distribution.

    Parameters:
        histogram: a list of the frequencies of the ones and tens digits 
        created by *ones_and_tens_digit_histogram*

    Returns:
        MSE of the given histogram with the uniform distribution.
    """
    return mean_squared_error(histogram, [0.10] * len(histogram))

def compare_mse_to_samples(mse, number_of_samples):
    """Given the MSE and the number of data points in the dataset, builds 10000 groups 
       of random numbers, each group with the same size as the election data. Computes 
       the MSE with the uniform distribution for each of these groups and Compares each 
       of these 10,000 MSEs to the MSE that was passed into the function as a parameter.
    
    Parameters:
       mse: mean squared error of the data's histogram with the uniform distribution
       number_of_samples: the number of samples in the dataset.

    Returns:
       equal_or_larger: how many of the 10,000 random MSEs are larger than or equal to the MSE of data
       smaller: how many of the 10,000 random MSEs are smaller than the MSE of data
    """ 
    equal_or_larger = 0
    smaller = 0
    for num in range(10000):
        group = random_group(number_of_samples)
        sample_mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(group))
        if sample_mse >= mse:
            equal_or_larger += 1
        else:
            smaller += 1
    return (equal_or_larger, smaller)

def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    """Given the Iranian MSE and the number of data points in the Iranian dataset,
       print out the quantity of MSEs larger than or equal to/smaller than the 2009 
       Iranian election MSE and 2009 Iranian election null hypothesis rejection level.
    
    Parameters:
        iranian_mse: mean squared error of the Iranian election's histogram with 
        the uniform distribution
        number_of_iranian_samples: the number of samples in the Iranian dataset.

    Returns:
        None
    """
    (equal_or_larger, smaller) = compare_mse_to_samples(iranian_mse, number_of_iranian_samples)
        
    print "Quantity of MSEs larger than or equal to the 2009 Iranian election MSE:",\
          equal_or_larger
    print "Quantity of MSEs smaller than the 2009 Iranian election MSE:",\
          smaller
    print "2009 Iranian election null hypothesis rejection level p:", \
          smaller / 10000.0    

################################################################################
# Problem 8: Comparing variation of samples
################################################################################        

def compare_us_mse_to_samples(us_mse, number_of_us_samples):
    """Given the US MSE and the number of data points in the US dataset,
       print out the quantity of MSEs larger than or equal to/smaller than the 2008 
       US election MSE and 2008 US election null hypothesis rejection level.
    
    Parameters:
        us_mse: mean squared error of the US election's histogram with 
        the uniform distribution
        number_of_us_samples: the number of samples in the US dataset.

    Returns:
        None
    """
    (equal_or_larger, smaller) = compare_mse_to_samples(us_mse, number_of_us_samples)
    
    print "Quantity of MSEs larger than or equal to the 2008 United States election MSE:",\
          equal_or_larger
    print "Quantity of MSEs smaller than the 2008 United States election MSE:",\
          smaller
    print "2008 United States election null hypothesis rejection level p:",\
          smaller / 10000.0

################################################################################
# Main Function
################################################################################

def main():
    """Main function, executed when fraud_detection.py is run as a Python
    script.
    """
    # Read and clean Iranian election data
    iranian_election_2009 = extract_election_vote_counts("election-iran-2009.csv",
    ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])

    # Read and clean US election data
    us_election_2008 = extract_election_vote_counts("election-us-2008.csv",
    ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])

    # Make a histogram for Iranian election data
    iraninian_histogram_2009 = ones_and_tens_digit_histogram(iranian_election_2009)
    
    # Make a histogram for US election data
    us_histogram_2008 = ones_and_tens_digit_histogram(us_election_2008)

    # Plot the election data for the Iranian election data
    plot_iranian_least_digits_histogram(iraninian_histogram_2009)

    # Plot the random data
    plot_distribution_by_sample_size()

    # Compute mean squared error of Iranian election with the uniform distribution 
    iranian_mse_with_uniform = calculate_mse_with_uniform(iraninian_histogram_2009)
    
    # Compute mean squared error of US election with the uniform distribution
    us_mse_with_uniform = calculate_mse_with_uniform(us_histogram_2008)

    print "2009 Iranian election MSE:", iranian_mse_with_uniform

    # Compare each of 10,000 groups' MSEs to to the Iranian MSE
    compare_iranian_mse_to_samples(iranian_mse_with_uniform, len(iranian_election_2009))

    print " "
    print "2008 United States election MSE:", us_mse_with_uniform

    # Compare each of 10,000 groups' MSEs to to the US MSE
    compare_us_mse_to_samples(us_mse_with_uniform, len(us_election_2008))

if __name__ == "__main__":
    main()