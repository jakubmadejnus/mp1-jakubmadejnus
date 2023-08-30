"""
Problem: Continuous Subarrays

Description:
Given a 0-indexed integer array `nums`, the task is to find the number of continuous 
subarrays. A subarray of `nums` is termed continuous if for any pair of indices `i1` and `i2` 
in the subarray, the absolute difference between `nums[i1]` and `nums[i2]` is no more than 2. 
The objective is to determine the total number of such continuous subarrays.

Function Signature:
def count_continuous_subarrays(nums: List[int]) -> int:

Inputs:
    - nums (List[int]): A list of integers.

Returns:
    - int: The total number of continuous subarrays.

Notes:
    - The definition of a subarray in this context refers to a contiguous, non-empty sequence of elements from the given array.
    - The absolute difference between any two numbers in a continuous subarray should not exceed 2.

Examples:

1. Input: nums = [5,4,2,4]
   Output: 8
   Explanation: 
   The continuous subarrays are: [5], [4], [2], [4], [5,4], [4,2], [2,4], and [4,2,4]. Total = 8.

2. Input: nums = [1,2,3]
   Output: 6
   Explanation: 
   The continuous subarrays are: [1], [2], [3], [1,2], [2,3], and [1,2,3]. Total = 6.

Hints:
    - One way to approach this problem is by using a two-pointer technique to evaluate each potential subarray.
    - For each subarray, iterate through its elements to ensure the condition of continuousness is met.

Tags:
    - Queue
"""

from typing import List

def count_continuous_subarrays(nums: List[int]) -> int:
    # TODO: Implement the function
    return 0
