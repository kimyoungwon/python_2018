# Name: Youngwon Kim
# CSE 160
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])

def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph(practice_graph)


###
### Problem 1b
###

rj = nx.Graph()

rj.add_edge("Nurse", "Juliet")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")
rj.add_edge("Romeo", "Friar Laurence")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Paris", "Mercutio")
rj.add_edge("Paris", "Escalus")

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])

def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
# draw_rj(rj)


###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given 
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    friends_set = set()
    for user_friends_name in friends(graph, user):
        friends_set = friends_set | friends(graph, user_friends_name)
    set_of_friends_of_friends = friends_set - friends(graph, user)
    set_of_friends_of_friends = set_of_friends_of_friends - set([user])
    return set_of_friends_of_friends

assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])

assert friends_of_friends(rj, "Juliet") == \
    set(['Mercutio', 'Paris', 'Escalus', 'Benvolio', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    return set(friends(graph, user1) & friends(graph, user2))

assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the 
    people who have at least one friend in common with the given user, 
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X" 
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }
    """
    dic_common_friends = dict()
    for name_of_friends_of_friends in friends_of_friends(graph, user):
        number_of_common_friends = 0
        for names_of_common_friends in common_friends(graph, user, name_of_friends_of_friends):
            number_of_common_friends = number_of_common_friends + 1
        dic_common_friends[name_of_friends_of_friends] = number_of_common_friends
    return dic_common_friends

assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 
      'Juliet': 1, 'Montague': 2 }
assert number_of_common_friends_map(rj, "Paris") == \
    {'Montague': 1, 'Tybalt': 1, 'Romeo': 1, 'Juliet': 1}

def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers, 
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    a = sorted(map_with_number_vals.items())
    sorted_by_high_value = sorted(a, key = itemgetter(1), reverse = True)
    sorted_keys = []
    for num in range(len(sorted_by_high_value)):
        sorted_keys.append(sorted_by_high_value[num][0])   
    return sorted_keys

assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == \
    ['c', 'a', 'd', 'e', 'b']

def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    set_number_of_common_friends_map = number_of_common_friends_map(graph, user)
    return number_map_to_sorted_list(set_number_of_common_friends_map)

assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']
assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their 
    influence score, with respect to the given user. The map only 
    contains people who have at least one friend in common with the given 
    user and are neither the user nor one of the users's friends. 
    See the assignment writeup for the definition of influence scores.
    """
    inf_map = dict()
    for name in friends_of_friends(graph, user):
        common = common_friends(graph, user, name)
        i_score = 0
        for name2 in common:
            num_friends_of_user_friends = len(friends(graph,name2))
            i_score = i_score + 1./num_friends_of_user_friends
        inf_map[name] = i_score
    return inf_map

assert influence_map(rj, "Mercutio") == \
    { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 
      'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }

def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    set_influence_map = influence_map(graph, user)   
    return number_map_to_sorted_list(set_influence_map)


assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###

print "Problem 4:"
print

unchanged_recommendations = []
changed_recommendations = []
for names in rj.nodes():
    if recommend_by_influence(rj, names) == recommend_by_number_of_common_friends(rj, names):
       unchanged_recommendations.append(names)
    else:
       changed_recommendations.append(names) 

print "Unchanged Recommendations:", sorted(unchanged_recommendations)
print "Changed Recommendations:", sorted(changed_recommendations)

###
### Problem 5
###

#Create a facebook graph
facebook = nx.Graph()

#Reading a file
myfile = open("facebook-links.txt")

# Process one line at a time and split the line 
all_facebook_data = []
for line_of_text in myfile:
    all_facebook_data.append(line_of_text.split())

#Extract 1st user and 2nd user as integers and then add them into edges of the facebook graph
user1 = []
user2 = []
for num in range(len(all_facebook_data)):
    user1.append(all_facebook_data[num][0])
    user1[num] = int(user1[num])
    user2.append(all_facebook_data[num][1])
    user2[num] = int(user2[num])
    facebook.add_edge(user1[num], user2[num])

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090
###
### Problem 6
###

print
print "Problem 6:"
print

# For every Facebook user with a user id that is a multiple of 1000, 
# print a list containing the first 10 friend recommendations by the number of common friends for Facebook

for user in sorted(facebook.nodes()):
    if user % 1000 == 0:
        recommended_common_friends = recommend_by_number_of_common_friends(facebook, user)
        print user ,"(by number_of_common_friends):", recommended_common_friends[0:10]

###
### Problem 7
###

print
print "Problem 7:"
print

# For every Facebook user with a user id that is a multiple of 1000, 
# print a list containing the first 10 friend recommendations by influence for Facebook

for user in sorted(facebook.nodes()):
    if user % 1000 == 0 :
        recommended_friends_by_influence = recommend_by_influence(facebook, user)
        print user ,"(by influence):", recommended_friends_by_influence[0:10]

###
### Problem 8
###

print
print "Problem 8:"
print

same_recommendations = []
different_recommendations = []
for users in sorted(facebook.nodes()):
    if users % 1000 == 0:
        recommended_common_friends = recommend_by_number_of_common_friends(facebook, users)
        recommended_friends_by_influence = recommend_by_influence(facebook, users)
        if recommended_common_friends[0:10] == recommended_friends_by_influence[0:10]:
            same_recommendations.append(users)
        else:
            different_recommendations.append(users)
      
print "Same:", len(same_recommendations)
print "Different:", len(different_recommendations)

###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").


