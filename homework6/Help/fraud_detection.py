# Name: Jeewon Ha
# UW NetID: haj7
# Section: AC
# CSE 160
# Homework 6: Fraud Detection

import csv
import matplotlib.pyplot as plt
import random

################################################################################
# Problem 1: Read and clean Iranian election data
################################################################################

def extract_election_vote_counts(filename, column_names):
    """Reads the CSV file at filename, and returns a list of integers.

    Parameters:
        filename: path to a CSV file.
        column_names: list of column names.

    Returns:
        list of integers: the values found in columns from every row.
        The order of the integers does not matter. 
    """
    vote_counts = []
    for row in csv.DictReader(open(filename)):
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
        numbers: list of numbers

    Returns:
        list of 10 numbers: index 'i' corressponding to frequency of digit
        'i' in the ones place or the thens place in the 'numbers'.
    """
    ones_and_tens = []
    for index in range(10):
        count = 0
        for number in numbers:
            if number % 100 / 10 == index:
                count += 1
            if number % 10 == index:
                count += 1
        ones_and_tens.append(count / (2.0 * len(numbers)))
    return ones_and_tens        
    

################################################################################
# Problem 3:
################################################################################

def plot_iranian_least_digits_histogram(histogram):
    """Given a histogram, graphs the frequencies for the Iranian election.

    Parameters:
        histogram: list of the frequencies of the ones and tens digits.

    Returns:
        None
    """
    plt.axis([0, 9, 0.06, 0.16])
    plt.plot([0.1] * 10, 'b-', label = 'Ideal')
    plt.plot(histogram, 'g-', label = 'Iran')
    plt.legend()
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.savefig("iran-digits.png")    


################################################################################
# Problem 4:
################################################################################

def plot_distribution_by_sample_size():
    """Plots the digit histograms for each of five collections of random
    numbers between 0 and 99.

    Parameters:
        None

    Returns:
        None
    """
    first = ones_and_tens_digit_histogram(random.sample(range(100), 10))
    second = ones_and_tens_digit_histogram(random.sample(range(100), 50))
    third = []
    for i in range(100):
        third.append(random.randint(0, 99))
    third = ones_and_tens_digit_histogram(third)
    fourth = []
    for i in range(1000):
        fourth.append(random.randint(0, 99))
    fourth = ones_and_tens_digit_histogram(fourth)
    fifth = []
    for i in range(10000):
        fifth.append(random.randint(0, 99))
    fifth = ones_and_tens_digit_histogram(fifth)
    plt.clf() # Deletes the previous plot
    plt.title('Distribution of last two digits')
    plt.plot([0.1] * 10, 'b-', label = 'Ideal')
    plt.plot(first, 'g-', label = '10 random numbers')
    plt.plot(second, 'm-', label = '50 random numbers')
    plt.plot(third, 'y-', label = '100 random numbers')
    plt.plot(fourth, 'r-', label = '1000 random numbers')
    plt.plot(fifth, 'c-', label = '10000 random numbers')
    plt.legend()
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.savefig("random-digits.png")


################################################################################
# Problem 5:
################################################################################

def mean_squared_error(numbers1, numbers2):
    """Given two graphs, returns the distance between two graphs.

    Parameters:
        numbers1: graph of f(x).
        numbers2: graph of g(x).

    Returns:
        distance between two datasets: mean squared error. The value is
        larger the more different the two graphs are. 
        - 0: if the two graphs are identical.
    """
    sum = 0.0
    for index in range(len(numbers1)):
        sum += (numbers1[index] - numbers2[index]) ** 2
    return sum / len(numbers1)   


################################################################################
# Problem 6:
################################################################################

def calculate_mse_with_uniform(histogram):
    """Given a histogram, returns the mean squared error of the histogram.

    Parameters:
        histogram: list of the frequencies of the ones and tens digits.

    Returns:
        mean squared error: distance between the given histogram and the
        uniform distribution.
    """
    return mean_squared_error(histogram, [0.1] * len(histogram))


def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    """Given MSE of the Iranian election and number of the samples, builds
    10000 groups of random numbers, each group with the same size as the
    Iranian election data(120), computes the MSE with the uniform distribution
    for each group, and compare each MSE to the given Iranian MSE.
    
    Parameters:
        iranian_mse: mean squared error of the Iranian election.
        number_of_iranian_samples: 120 samples in the Iranian dataset.

    Returns:
        None
    """
    count_equal_larger = 0
    count_smaller = 0
    for num_of_group in range(10000):
        group_random = []
        for index in range(number_of_iranian_samples):
            group_random.append(random.randint(0, 99))
        mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(group_random))
        if mse >= iranian_mse:
            count_equal_larger += 1
        else:
            count_smaller += 1
    print 'Quantity of MSEs larger than or equal to the 2009 Iranian election MSE:',\
          count_equal_larger
    print 'Quantity of MSEs smaller than the 2009 Iranian election MSE:',\
          count_smaller
    print '2009 Iranian election null hypothesis rejection level p:', \
          count_smaller / 10000.0


################################################################################
# Problem 8:
################################################################################

def compare_us_mse_to_samples(us_mse, number_of_us_samples):
    """Given MSE of the US election and number of the samples, builds 10000
    groups of random numbers, each group with the same size as the
    US election data, computes the MSE with the uniform distribution
    for each group, and compare each MSE to the given US MSE.
    
    Parameters:
        us_mse: mean squared error of the US election.
        number_of_us_samples: number of samples in the US dataset.

    Returns:
        None
    """
    count_equal_larger = 0
    count_smaller = 0
    for num_of_group in range(10000):
        group_random = []
        for index in range(number_of_us_samples):
            group_random.append(random.randint(0, 99))
        mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(group_random))
        if mse >= us_mse:
            count_equal_larger += 1
        else:
            count_smaller += 1
    print 'Quantity of MSEs larger than or equal to the 2008 United States election MSE:',\
          count_equal_larger
    print 'Quantity of MSEs smaller than the 2008 United States election MSE:',\
          count_smaller
    print '2008 United States election null hypothesis rejection level p:',\
          count_smaller / 10000.0


################################################################################
# Main Function
################################################################################

def main():
    """Main function, executed when fraud_detection.py is run as a Python
    script.
    """
    # Read and clean Iranian election data
    iran_2009 = extract_election_vote_counts("election-iran-2009.csv",
    ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])

    # Read and clean US election data
    us_2008 = extract_election_vote_counts("election-us-2008.csv",
    ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])

    # Compute the frequencies of index 'i' in digit 'i' for Iranian election data
    frequency_2009 = ones_and_tens_digit_histogram(iran_2009)
    
    # Compute the frequencies of index 'i' in digit 'i' for US election data
    frequency_2008 = ones_and_tens_digit_histogram(us_2008)

    # Plot the frequencies for the Iranian election data
    plot_iranian = plot_iranian_least_digits_histogram(frequency_2009)

    # Plot the frequencies for
    plot_random = plot_distribution_by_sample_size()

    # Compute difference/distance between two datasets
    distance = mean_squared_error([1, 4, 9], [6, 5, 4])

    # Compute mean squared error of Iranian election with the uniform distribution 
    iran_mse_with_uniform = calculate_mse_with_uniform(frequency_2009)
    
    # Compute mean squared error of US election with the uniform distribution
    us_mse_with_uniform = calculate_mse_with_uniform(frequency_2008)

    print '2009 Iranian election MSE:', iran_mse_with_uniform

    # Compare mse of Iranian election with mse of groups with random numbers
    compare_iranian_mse_to_samples(iran_mse_with_uniform, 120)

    print ''
    print '2008 United States election MSE:', us_mse_with_uniform

    # Compare mse of US election with mse of groups with random numbers
    compare_us_mse_to_samples(us_mse_with_uniform, 120)

if __name__ == "__main__":
    main()


        
print extract_election_vote_counts("election-iran-2009.csv",["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]