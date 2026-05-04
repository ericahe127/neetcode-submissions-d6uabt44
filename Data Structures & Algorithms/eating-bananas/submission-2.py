class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best_rate = r

        while l <= r:
            mid = (l+r) // 2
            time = 0
            for x in piles:
                time += math.ceil(x / mid)

            if time <= h:
                r = mid - 1
                best_rate = min(best_rate, mid)
            else:
                l = mid + 1
        return best_rate

        