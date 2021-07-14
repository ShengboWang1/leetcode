class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.size = 0



    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        self.size += 1


    def findMedian(self) -> float:
        s = self.size
        if s % 2 == 0:
            return (self.nums[(s - 1)// 2] + self.nums[(s - 1) // 2 + 1])/2
        else:
            return self.nums[s // 2]