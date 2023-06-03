# Assignment 6 - String Mapping Problem

This repository contains a Python solution for the string mapping problem.

## Problem Statement

The problem involves mapping a set of strings to each other using a conversion function and calculating the matching cost between them. The conversion function can introduce dashes to the original string, and the matching cost is determined by the characters' pairwise comparison. The goal is to find the conversion with the lowest final cost.

## Solution

The solution is implemented in Python and consists of the following components:

1. `cost_of_conversion(string, CC)`: A function that calculates the cost of conversion for a given string based on the introduction of dashes. It takes the string and the conversion cost constant as input.

2. `cost_of_matching(string1, string2, MC)`: A function that calculates the cost of matching between two strings by comparing characters. It takes two strings and a matching cost matrix as input.

3. `cost_of_mapping(strings, CC, MC)`: A function that calculates the total cost of mapping for a set of strings. It iterates over the strings to calculate the conversion costs and pairwise matching costs. It takes the strings, conversion cost constant, and matching cost matrix as input.

4. `find_optimal_mapping(strings, CC, MC)`: A function that finds the optimal mapping by iteratively adding dashes to the strings and selecting the mapping with the lowest cost. It takes the strings, conversion cost constant, and matching cost matrix as input.

The main function prompts the user to input the number of strings, the strings themselves, the conversion cost, the matching cost matrix, and the vocabulary. It then calls the `find_optimal_mapping` function to obtain the optimal mapping and prints the result.

## Input Format

![image](https://github.com/pratt-sark/ai/assets/72748736/eafaf022-548a-4e8a-a138-5490e9ad755f)

### Issues

The code is possibly doing an exhaustive search, generating all possible dash positions bounded by some integer length in each iteration. The executiion is going on forever, so can't verify if its correct or not. I couldn't implement better strategies within the given time frame... This is all I have for you to consider in case of evaluation of this assignment.
