class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        ans = [""] * n
        while l < r:
            while l < r and not self.isValid(s[l]):
                ans[l] = s[l]
                l += 1
            while l < r and not self.isValid(s[r]):
                ans[r] = s[r]
                r -= 1
            ans[l], ans[r] = s[r], s[l]
            l += 1
            r -= 1

        if l == r:
            ans[l] = s[l]

        return "".join(ans)

    def isValid(self, ch):
        if (ch >= 'a' and ch <='z') or (ch >= 'A' and ch <='Z'):
            return True
        else:
            return False