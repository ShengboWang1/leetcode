class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = 0, 0
        for i in range(len(weights)):
            right += weights[i]
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if self.isValid(weights, days, mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def isValid(self, weights, days, value):
        weight_one_time = 0
        count = 0
        i = 0
        while i <= len(weights) - 1:
            if weights[i] > value:
                return False
            while i <= len(weights) - 1 and weight_one_time + weights[i] <= value:
                weight_one_time += weights[i]
                i += 1
            count += 1
            weight_one_time = 0
        return count <= days