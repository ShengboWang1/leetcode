class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set = [0] * 26
        for i in range(len(s)):
            set[ord(t[i]) - ord("a")] += 1
            set[ord(s[i]) - ord("a")] -= 1

        for i in range(26):
            if set[i] != 0:
                return False

        return True