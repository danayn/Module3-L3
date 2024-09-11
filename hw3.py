#Assignments: Python Sets
'''
1. Python Sets Adventure

Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

'''

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Destinations that both airlines fly to.
bothfly = our_routes.intersection(competitor_routes)
print("The Destination/Destinations that both airlines fly to is/are "+str(bothfly)+".")
print()

#Destinations unique to your airline.
uniquefly = our_routes.difference(competitor_routes)
print("The Destination/Destinations that is unique to our airline is/are "+str(uniquefly)+".")
print()

#Whether there are any destinations that neither airline shares.
share = our_routes.isdisjoint(competitor_routes)
print("For the question of,'Do both airlines don't share a destination?',--- the answer is "+str(share)+".")