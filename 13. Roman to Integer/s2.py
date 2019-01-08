#sample solution using hash map (dict)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = i = 0
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        integer = [1, 5, 10, 50, 100, 500, 1000]
        lookup = dict(zip(roman, integer))
        while i < len(s) - 1:
            if lookup[s[i+1]] > lookup[s[i]]:
                ans, i = ans + lookup[s[i+1]] - lookup[s[i]], i + 2
            else:
                ans, i = ans + lookup[s[i]], i + 1
        if i == len(s) -1: 
            ans += lookup[s[-1]]
        return ans
