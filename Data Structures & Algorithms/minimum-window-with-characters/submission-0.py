class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countT = {}
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
            
        resLen = float("inf")
        res = [0, 0]
        have = 0
        need = len(countT)  # Fixed: need unique characters count, not len(t)
        countS = {}
        l = 0

        for r in range(len(s)):
            poki = s[r]
            countS[poki] = 1 + countS.get(poki, 0)

            if poki in countT and countS[poki] == countT[poki]:
                have += 1

            while have == need:
                if resLen > (r - l + 1):
                    resLen = r - l + 1
                    res = [l, r]

                # Fixed: update countS using s[l], not countT[l]
                leftChar = s[l]
                countS[leftChar] -= 1
                if leftChar in countT and countS[leftChar] < countT[leftChar]:
                    have -= 1
                l += 1

        # Fixed: float("inf") and string slicing with colon and +1
        return s[res[0]:res[1] + 1] if resLen != float("inf") else ""