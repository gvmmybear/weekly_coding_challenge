# Author: Christian Castro
# Date: 06/07/2022
# Coding Challenge Revature:  Week of June 7th 2022


def main():
    # Sample input from problem 1 statement
    nums_1 = [1, 2, 3]   # expected: 2
    nums_2 = [10, 15, 5]    # expected: 10
    nums_3 = [100, 999, 500]    # expected: 500
    triples_input = [nums_1, nums_2, nums_3]
    # p1_input_size = 3
    print("PROBLEM 1 SOLUTION OUTPUT:")
    solution_problem_1(triples_input)

    # Sample input from problem 2 statement
    alpha_num_str = "ab1231da"
    print("\nPROBLEM 2 SOLUTION INPUT:", alpha_num_str)
    print("PROBLEM 2 SOLUTION OUTPUT:", solution_problem_2(alpha_num_str))

# Problem 1
# Problem Statement
# Write a program that accepts sets of three numbers, and prints the 
# second-maximum number among the three.
# 
# Input
#  - First line contains the number of triples, N.
#  - The next N lines which follow each have three space separated integers. 
# Output
#  - For each of the N triples, output one new line which contains the 
#    second-maximum integer among the three.
# 
# Constraints
#   - 1 ≤ N ≤ 6
#   - 1 ≤ every integer ≤ 10000
#   - The three integers in a single triplet are all distinct. 
#     That is, no two of them are equal.
def solution_problem_1(nums):
    # iterates through the triples input and sorts then appends 
    # index 1 which is second largest value, to return arr.
    return_array = []
    for i in range(len(nums)):
        nums[i].sort()
        return_array.append(nums[i][1])

    # result array is printed and returned 
    for i in range(len(return_array)):
        print(return_array[i])
    return return_array

# Problem 2
# Problem statement
# Given an alphanumeric string made up of digits and lower case Latin characters 
# only, find the sum of all the digit characters in the string.
#
# Input
#   - The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow.
#   - Each test case is described with a single line containing a string S, the alphanumeric string.
# Output
#   - For each test case, output a single line containing the sum of all the digit characters in that string.
# Constraints
#   - 1 ≤ T ≤ 1000
#   - 1 ≤ |S| ≤ 1000, where |S| is the length of the string S.
def solution_problem_2(str):
    sum = 0
    for char in str:
        if char.isdigit():
            sum += (int(char))
    return sum


if __name__ == "__main__":
    main()