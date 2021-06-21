class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)

        if not digits:
            digits = [1]

        elif digits[length - 1] != 9:
            digits[length - 1] += 1
        else:
            digits[length - 1] = 0
            digits[:-1] = self.plusOne(digits[:-1])

        return digits