class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = nums[0]
        while left <= right:
            mid = (left + right) >> 1
            # 如果这个数比最右面的小 那他有可能是答案
            # 看这个数在第一个 或者他的左面的数 比他大 那就是他了
            # 如果他左面的数比他还小 那再往左
            if nums[mid] < nums[len(nums) - 1]:
                if mid == 0 or nums[mid - 1] > nums[mid]:
                    return nums[mid]
                else:
                    right = mid - 1
            # 如果这个数大了 那往右找
            elif nums[mid] >nums[right]:
                left = mid + 1
            # 如果这个数nums[mid] 正好等于最右面的数
            # 第一种情况 找到的nums[mid]与nums[right]下标相同 直接返回他
            # 第二种情况 找到的nums[mid]与nums[right]下标不同 有重复元素
            # right -= 1
            else:
                if mid == right:
                    return nums[mid]
                else:
                    right -= 1