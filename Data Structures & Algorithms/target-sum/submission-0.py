class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Our cache to store states we've already seen
        # Key: (index, current_sum) -> Value: number of ways to reach target from here
        memo = {}

        def dfs(index, current_sum):
            # Base Case: We've processed all numbers in the array
            if index == len(nums):
                # If our sum matches the target, we found 1 valid path!
                if current_sum == target:
                    return 1
                return 0
            
            # If we have already calculated this exact state, return the saved answer
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # Choice 1: Add the current number
            add_ways = dfs(index + 1, current_sum + nums[index])
            
            # Choice 2: Subtract the current number
            subtract_ways = dfs(index + 1, current_sum - nums[index])

            # The total ways from this state is the sum of both choices
            memo[(index, current_sum)] = add_ways + subtract_ways
            
            return memo[(index, current_sum)]

        # Start the recursion at index 0, with a running sum of 0
        return dfs(0, 0)