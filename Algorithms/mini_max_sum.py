"""
======================================= Exercise Minim_Max_Sum =======================================================
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of
the five integers. Then print the respective minimum and maximum values as a single line of
two space-separated long integers.

-------------------------------------------- Example ------------------------------------------------
arr = [1,3,5,7,9]
The minimum sum is  1+3+5+7 = 16 and the maximum sum is 3+5+7+9= 24. The function prints

16 24

---------------------------------------- Function Description --------------------------------------
Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

   * arr: an array of

   * integers

--------------------------------------------- Print --------------------------------------------
Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

------------------------------------------ Input Format ------------------------------------------
A single line of five space-separated integers.

------------------------------------------- Constraints -------------------------------------------------------
1<= arr[i] <= 10^⁹

------------------------------------------ Output Format ------------------------------------------------------------

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by
summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
"""


# !/bin/python3


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s = sum(arr)
    print(str(s - max(arr)) + " " + str(s - min(arr)))


if __name__ == '__main__':
    In = int(input())
    for i in range(In):
        arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
