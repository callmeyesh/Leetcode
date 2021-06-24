"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

1st [2,1,0,1,3]
    [  1,2,1 ]
max = 2

2nd [3,2,1,2,1]
[0,0,1,0,0]

l=1, r=0

[0,1,0,2,1,0,1,4,2,1,2,1]
     l  r

                  2 1      min = curr or min(l or r)
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Input: height = [4,2,0,3,2,5]
Output: 9

"""
import heapq
import math
class Solution:
    def __init__(self):
        pass

    def rain_water(self, nums):
        res = 0
        #res += self.start(nums)
        #print(res)
        res += self.start(list(reversed(nums)))
        return res


    def start(self, nums):
        left, right, res  = 0, 1, 0
        while left < len(nums):
            #[4,2,0,3,2,5]
            #[0,2,4,1,2]

            #[5,2,3,0,2,4]
            while right < len(nums) and nums[left] >= nums[right]:
                right += 1
            #if nums[left] > nums[right]:
            res += self.calculate(left, right - 1, nums)
            left = right
        return res


    def calculate(self, left, right, nums):
        print(left, right)
        capacity = 0
        bound = nums[left]
        while left <= right:
            #print(bound , nums[left])
            if bound != nums[left]:
                capacity += bound - nums[left]
            left += 1

        return capacity





if __name__ == "__main__":
    s = Solution()
    print(s.rain_water([4,2,0,3,2,5]))
