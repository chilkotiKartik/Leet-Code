from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target:
                    left += 1
                elif curr > target:
                    right -= 1
                else:
                    return curr

        return closest