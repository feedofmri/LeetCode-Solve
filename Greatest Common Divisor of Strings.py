class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return 0
            size1, size2 = len1 // l, len2 // l
            return str1[:l] * size1 == str1 and str1[:l] * size2 == str2
        
        for l in range(min(len1, len1), 0, -1):
            if(isDivisor(l)):
                return str1[:l]
        return ""

        