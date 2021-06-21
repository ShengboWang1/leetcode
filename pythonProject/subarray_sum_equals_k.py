class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [nums[0]] * (len(nums))
        count = dict()
        ans = 0

        # 求前缀和
        for i in range(1, len(nums)):
            sums[i] = sums[i - 1] + nums[i]

        # 或者是s[r] - s[l-1] == k 或者是s[r]==k
        for i in range(len(nums)):
            if sums[i] == k:
                ans += 1
            if sums[i] - k in count:
                ans += count[sums[i] - k]
            count[sums[i]] = count.get(sums[i], 0) + 1

        return ans