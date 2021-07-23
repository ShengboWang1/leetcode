class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                break
            if self.isValid(piles, h, mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
    def isValid(self, piles, h, K):
        piles = piles[:]
        count = 0
        i = 0
        while i <= len(piles) - 1:
            count += piles[i] // K
            if piles[i] % K != 0:
                count += 1
            i += 1
        return count <= h