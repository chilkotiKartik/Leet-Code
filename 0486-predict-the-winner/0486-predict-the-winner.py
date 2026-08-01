class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        memo = {}

        def max_diff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Take left element or take right element
            pick_left = nums[i] - max_diff(i + 1, j)
            pick_right = nums[j] - max_diff(i, j - 1)
            
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        return max_diff(0, len(nums) - 1) >= 0