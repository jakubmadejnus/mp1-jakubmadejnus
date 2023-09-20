"""
Problem: Two Sum

Given an array of numbers sorted in ascending order and a target sum, find a pair in the array 
whose sum is equal to the given target. You must solve this using O(1) space. 

Function Signature:
def two_sum(arr: List[int], target: int) -> List[int]:

Inputs:
    - arr (List[int]): A list of integers sorted in ascending order.
    - target (int): An integer representing the target sum.

Returns:
    - List[int]: A list containing the indices of the two numbers that add up to the target sum.
                 If no such pair exists, return an empty list.

Examples:

1. Input: arr = [1, 2, 3, 4, 6], target = 6
   Output: [1, 3]
   Explanation: 2 and 4 in the list add up to the target sum of 6.

2. Input: arr = [2, 5, 9, 11], target = 11
   Output: [0, 2]
   Explanation: 2 and 9 in the list add up to the target sum of 11.

3. Input: arr = [1, 2, 3, 4], target = 10
   Output: []
   Explanation: No pairs in the list add up to the target sum of 10.

Note:
The function should be able to handle the cases where there is exactly one valid pair 
that adds up to the target sum, as shown in the examples above.

Hint: 
  - Use the two pointer approach.

Tags:
  - Array
  - Two Pointers
"""

from typing import List

def two_sum(arr: List[int], target: int) -> List[int]:

   # what the program already has

   # the first pointer
   i = 0

   # the second pointer
   j = len(arr) - 1

   while i < j:
        # If we find a solution, print solution
        if arr[i] + arr[j] == target:
            return [i, j]
        
        # If sum of elements at current pointers is less, we move towards higher values by doing i++
        elif arr[i] + arr[j] < target:
            i += 1
 
        # If sum of elements at current pointers is more, we move towards lower values by doing j--
        else:
            j -= 1
 
   return []

