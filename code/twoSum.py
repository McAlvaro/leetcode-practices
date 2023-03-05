"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
-----------------------------------------------------------------
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
------------------------------------------------------------------
Ref: https://leetcode.com/problems/two-sum/description
Tag: Easy
"""
def twoSum(nums, target):
  numToIndex = {}
  for i in range(len(nums)):
    print(nums[i])
    if target - int(nums[i]) in numToIndex:
      return [numToIndex[target - int(nums[i])], i]
    numToIndex[int(nums[i])] = i
  return []

_nums = input().split(',')
_target = int(input())

print( twoSum(_nums, _target) )
