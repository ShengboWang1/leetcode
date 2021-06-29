class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] = [hashmap[nums[i]][0] + 1, hashmap[nums[i]][1], i]
            else:
                hashmap[nums[i]] = [1, i, i]
        ans = len(nums)
        max_times = 1
        for times, left, right in hashmap.values():
            if times > max_times:
                max_times = times
                ans = right - left + 1
            if times == max_times:
                ans = min(ans, right - left + 1)

        return ans