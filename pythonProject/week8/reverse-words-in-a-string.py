class Solution:
    def reverseWords(self, s: str) -> str:

        temp = s.split(" ")
        while temp[0] == "":
            temp.pop(0)

        while temp[-1] == "":
            temp.pop()
        n = len(temp)
        l, r = 0, n - 1
        while l < r:
            temp[l], temp[r] = temp[r], temp[l]
            l += 1
            r -= 1
        return " ".join(temp)