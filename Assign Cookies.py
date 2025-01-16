class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c = 0
        j = 0
        while j < len(s) and c < len(g):
            if s[j] >= g[c]:
                c += 1
            j += 1
        return c