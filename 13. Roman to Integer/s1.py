class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_value = 0
        digit_value = 0
        
        for i in range(len(s)):
            
            value = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            digit_value = value.get(s[i], '0') #set to 0 by default, incl. Char not found           
            
            
            if (i+1 < len(s)):
                if s[i] =='I' and ((s[i+1]=='V') or (s[i+1]=='X')):
                    digit_value = -1 *digit_value
                if s[i] =='X' and ((s[i+1]=='L') or (s[i+1]=='C')):
                    digit_value = -1 *digit_value
                if s[i] =='C' and ((s[i+1]=='D') or (s[i+1]=='M')):
                    digit_value = -1 *digit_value
            
            total_value+=digit_value
            
            #print(digit_value)
            
        #print(total_value)
        
        return total_value
