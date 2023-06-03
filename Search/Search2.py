# Problem Statement: There are K strings Xi from the vocabulary V. Each string Xi has length Ni. Your goal is to map
# the strings to each other. An easy way to do this is to think of this in two steps – conversion and matching. Conversion
# is a function F that takes in a string and returns another string. All F(Xi)s have the same length N. N is greater than
# equal to all Nis. The function F is only allowed to make one change to the original string – it can introduce dashes. It
# can introduce any number of dashes at any position. The conversion cost of X to F(X) is CC*number of dashes, CC being
# a constant. Once all strings have been converted the matching step just matches characters at each position. The
# matching cost between two characters is given by a symmetric function MC(c1, c2) where c1 and c2 are two characters
# ϵ V U {-}. Matching cost of two strings is the sum of matching costs of their conversions at each position. Finally, the
# matching cost of K strings is the sum of pairwise matching costs between each pair.
# Example: Let K =3. Let vocabulary V= {A,C,T,G}. Suppose the three strings Xis are:
# X1: ACTGTGA
# X2: TACTGC
# X3: ACTGA
# So, for this problem N1, N2, N3 are 7, 6 and 5 respectively. Let all costs be as follows: CC = 3, MC(x,y) = 2 if x, y ϵ V and
# x != y; MC(x, -) = 1; MC(x, x) = 0. We may define our conversions as follows:
# F(X1): -ACTGTGA
# F(X2): TACT--GC
# F(X3): -ACTG--A
# With these conversions N = 8. The conversion costs are respectively 3, 6, and 9. The matching cost between F(X1) and
# F(X2) is 1+0+0+0+1+1+0+2 = 5. Similarly between F(X2) and F(X3) is 1+0+0+0+1+0+1+2=5 and between F(X1) and F(X3) is
# 0+0+0+0+0+1+1+0=2. Hence the total matching cost of this conversion is 5+5+2=12.
# The final output cost of this mapping problem is sum of conversion and matching costs = 3+6+9+12=30.
# Your goal is to find a conversion with the lowest final cost. (The current solution is not the optimal solution for this
# problem)

import numpy as np

# Function to calculate the cost of conversion
def cost_of_conversion(string, CC):
    cost = 0
    for i in range(len(string)):
        if string[i] == '-':
            cost += CC
    return cost

# Function to calculate the cost of matching
def cost_of_matching(string1, string2, MC):
    cost = 0
    for i in range(min(len(string1),len(string2))):
        if string1[i] == '-' or string2[i] == '-':
            cost += 1
        else:
            cost += MC[string1[i]][string2[i]]
    return cost

# Function to calculate the cost of mapping
def cost_of_mapping(strings, CC, MC):
    cost = 0
    for i in range(len(strings)):
        cost += cost_of_conversion(strings[i], CC)
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            cost += cost_of_matching(strings[i], strings[j], MC)
    return cost

# function to find the optimal mapping. First, start with limit = length of the longest string.
# Add any number of dashes in any position in the strings to make them of equal length.
# Then, find the optimal mapping. Re iterate the process using an increased number of dashes.
# Stop when the length reaches 8 or mapping cost starts increasing. 
# Example Input: K = 3, CC = 3, MC = {A: {A: 0, C: 2, T: 2, G: 2, '-': 1}, C: {A: 2, C: 0, T: 2, G: 2, '-': 1}, T: {A: 2, C: 2, T: 0, G: 2, '-': 1}, G: {A: 2, C: 2, T: 2, G: 0, '-': 1}, '-': {A: 1, C: 1, T: 1, G: 1, '-': 0}}, V = ['A', 'C', 'T', 'G']
# Input Strings: ['ACTGTGA', 'TACTGC', 'ACTGA']
# Example output: -ACTGTGA, TACT--GC, -ACTG--A

def find_optimal_mapping(strings, CC, MC):
    # find the length of the longest string
    max_len = 0
    for i in range(len(strings)):
        if len(strings[i]) > max_len:
            max_len = len(strings[i])
    # add dashes to make the strings of equal length
    for i in range(len(strings)):
        strings[i] = strings[i] + '-'*(max_len - len(strings[i]))
    # find the optimal mapping
    while len(strings[0]) < 8:
        # create a list of all possible strings
        possible_strings = []
        for i in range(len(strings)):
            for j in range(len(strings[i])):
                possible_strings.append(strings[i][:j] + '-' + strings[i][j:])
            possible_strings.append(strings[i] + '-'*len(strings[i]))
        # find the optimal mapping
        min_cost = np.inf
        for i in range(len(possible_strings)):
            temp_strings = strings[:]
            temp_strings.append(possible_strings[i])
            temp_cost = cost_of_mapping(temp_strings, CC, MC)
            if temp_cost < min_cost:
                min_cost = temp_cost
                optimal_string = possible_strings[i]
        strings.append(optimal_string)
    return strings

# main function
if __name__ == '__main__':
    # take input from the user
    K = int(input('Enter the number of strings: '))
    strings = []
    for i in range(K):
        strings.append(input('Enter string ' + str(i+1) + ': '))
    CC = int(input('Enter the conversion cost: '))
    MC = {}
    V = input('Enter the vocabulary: ').split()
    for i in range(len(V)):
        MC[V[i]] = {}
        for j in range(len(V)):
            MC[V[i]][V[j]] = int(input('Enter the matching cost between ' + V[i] + ' and ' + V[j] + ': '))

    # find the optimal mapping
    strings = find_optimal_mapping(strings, CC, MC)

    # print the optimal mapping
    print('The optimal mapping is:')
    for i in range(len(strings)):
        print(strings[i])
    print('The cost of mapping is:', cost_of_mapping(strings, CC, MC))