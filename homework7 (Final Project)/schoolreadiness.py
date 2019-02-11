# Name: Youngwon Kim
# UW NetID: 1724787
# CSE 160
# Homework 7: Final Project

import csv
import scipy.stats as sp
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

import pandas as pd
from pandas import DataFrame

################################################################################
# Step 1: Read and clean Korean Earlychildhood data
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

def number_of_variables(dataset, name_of_variable):
    """Reads 1st row of the dataset, and returns the number of certain 
       variables in a dataset

    Parameters:
        dataset: a list of a dataset created by *read_csv*
        name_of_variable: a variable name in a dataset
        
    Returns:
        Number of variables: Count the frequencies of a certain variable name at 
        the first row in a dataset
    """
    first_row = dataset[0].keys()
    num = 0
    for variable in first_row:
        if name_of_variable in variable:
            num += 1   
    return num  

def means_of_variables(dataset, name_of_variable):
    """Given a list of a dataset, returns a dictionary including variable name and values 

    Parameters:
        dataset: a list of a dataset created by *read_csv*
        name_of_variables: a variable name in a dataset
        
    Returns:
        list of means: The values related to name_of_variable can be found in every row 
        of a list of dictionaires. The order of the integers matters. If the sum of items of variables
        is 0, the value will be ignored.
    """
    list_of_means = []
    for num in range(len(dataset)):
        sum_of_variables = 0
        for row in dataset[num].items():
            if name_of_variable in row[0]:
                if row[1].strip() != "":
                    sum_of_variables += int(row[1])
        if sum_of_variables != 0:
            list_of_means.append(float(sum_of_variables) / number_of_variables(dataset, name_of_variable))                     
    return list_of_means

def make_a_new_dict(dataset, names_of_variables):
    """Given a list of a dataset, returns a dictionary including variable name and values 

    Parameters:
        dataset: a list of a dataset created by *read_csv*
        names_of_variables: a variable name or variable names in a dataset
        
    Returns:
        new_dict:A dictionary including all cleaned data. The orders in a dictionary does not matters. 
    """
    new_dict = {}
    for variable_name in names_of_variables:
        new_dict[variable_name] = means_of_variables(dataset, variable_name)
    return new_dict

def count_gender(dictionary, gender_variable):
    """Given a dictionary, returns numbers of boys and girls 

    Parameters:
        dictionary: a dictionary created by *make_a_new_dict*
        gender_variable: a variable name containing gender
        
    Returns:
        boy, girl :The numbers of boys and girls in the gender_variable. 
    """
    boy = 0
    girl = 0
    for num in dictionary[gender_variable]:
        if num == 1:
            boy += 1
        elif num == 2:
            girl += 1
    return (boy, girl)
    
def get_pearsonr(dictionary,names_of_variables):
    """Given a dictionary, get the corrleations and their p-value of names_of_variable

    Parameters:
        dictionary: a dictionary created by *make_a_new_dict*
        names_of_variables: a variable name or variable names in a dataset
        
    Returns:
        None
    """
    num = 0
    for variable1 in names_of_variables:
        num += 1
        for variable2 in names_of_variables[num:]:
            if variable1 != variable2:
                correlation = sp.pearsonr(dictionary[variable1], dictionary[variable2])
                print "The significance (p) of correlation "+ "("+ str(correlation[0]) + ")" + \
                " between " + variable1 + " and "  + variable2 + ": " + str(correlation[1])

def bar_grapgh(dictionary, variable):
    """Given a histogram, graphs the frequencies of each variable for the Korean ecec data

    Parameters:
        dictionary: a dictionary created by *make_a_new_dict*
        variable: a name of variable

    Returns:
        None
    """
    plt.clf() # Deletes the previous plot    
    plt.hist(dictionary[variable])
    plt.title('Histogram of ' + variable)
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.savefig(variable)

def scatter_plot(dictionary, variable1, variable2):
    """Given a scatter plot, make spots of two variables for the Korean ecec data

    Parameters:
        dictionary: a dictionary created by *make_a_new_dict*
        variable1: a name of variable
        variable2: a name of variable

    Returns:
        None
    """    
    plt.clf() # Deletes the previous plot    
    plt.scatter(dictionary[variable1], dictionary[variable2],  color='purple')
    plt.title('Scatter plot between ' + variable1 + " and " + variable2)
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.savefig(variable1 + " and " + variable2)

################################################################################
# Main Function
################################################################################

def main():
    """Main function, executed when fraud_detection.py is run as a Python
    script.
    """
    # Read and clean Korean ECEC data
    data = read_csv('project_data.csv')
    
    # Make a dictionary of necessary variables for analysis
    new_dict = make_a_new_dict(data,['Family_Income','Gender', 'Interaction','Self_Regulation','School_Readiness'])
    
    # Change a dictionary into a dataframe
    new_dataframe = pd.DataFrame.from_dict(new_dict)
    
    # Count the number of boys and girls and get gender ratio
    number_of_boys_and_girls = count_gender(new_dict, 'Gender')
    number_of_boys = number_of_boys_and_girls[0]
    number_of_girls = number_of_boys_and_girls[1]
    ratio_of_girls = float(number_of_girls)/(number_of_boys + number_of_girls)
    print "#######"
    print "Gender"
    print "#######"
    print ""
    print "The number of boys is " + str(number_of_boys) + " and the number of girls is " + str(number_of_girls) + \
    ". The ratio of girls is " + str(ratio_of_girls) + "."
    print ""
    
    # Show frequencies, means, standard deviations, min/max numbers
    print "#######################"
    print "Descriptive Statistics"
    print "#######################"
    print ""
    print new_dataframe[['Family_Income','Interaction','Self_Regulation','School_Readiness']].describe()
    
    # Show a correlation matrix between variables
    print ""
    print "#############"
    print "Correlations"
    print "#############"
    print ""
    print new_dataframe[['Family_Income','Interaction','Self_Regulation','School_Readiness']].corr(method = 'pearson')
 
    # Check how significant correlations are 
    print ""
    print "#############################"
    print "Signficances of Correlations"
    print "#############################"
    print ""
    get_pearsonr(new_dict, ['Family_Income','Interaction','Self_Regulation', 'School_Readiness'])

    # Show histgrams of variables
    bar_grapgh(new_dict, 'Family_Income')
    bar_grapgh(new_dict, 'Interaction')
    bar_grapgh(new_dict, 'Self_Regulation')
    bar_grapgh(new_dict, 'School_Readiness')

    # Show scatter_plots between variables    
    scatter_plot(new_dict, 'Family_Income', 'Interaction')
    scatter_plot(new_dict, 'Family_Income', 'Self_Regulation')
    scatter_plot(new_dict, 'Family_Income', 'School_Readiness')
    scatter_plot(new_dict, 'Interaction','Self_Regulation')
    scatter_plot(new_dict, 'Interaction','School_Readiness')
    scatter_plot(new_dict, 'Self_Regulation', 'School_Readiness')
    
    # Regression and show a quantile-quantile plot
    reg = smf.ols('School_Readiness ~ Family_Income + Interaction + Self_Regulation', data = new_dataframe)
    res = reg.fit()
    plt.clf() # Deletes the previous plot    
    sm.qqplot(res.resid).show()
    print ""
    print "#############"
    print "Regression"
    print "#############"
    print ""
    print(res.summary())

if __name__ == "__main__":
    main()
