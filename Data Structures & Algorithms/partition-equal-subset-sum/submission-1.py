class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        dp = set()
        dp.add(0)

        for x in nums:
            tmp = set()
            for cur_sum in dp:
                new_sum = cur_sum + x

                if new_sum == target:
                    return True

                tmp.add(new_sum)
                tmp.add(cur_sum)

            dp = tmp

        
        return False

                
        