class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        numS, numT = {}, {}

        for i in range(len(s)):
            numS[s[i]] = 1 + numS.get(s[i], 0)
            numT[t[i]] = 1 + numT.get(t[i], 0)

        return numS == numT