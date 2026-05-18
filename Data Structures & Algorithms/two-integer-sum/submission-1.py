class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sol:
                return [sol[diff], i]
            sol[n] = i