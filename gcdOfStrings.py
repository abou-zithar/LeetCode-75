class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenation of the strings in both orders is not equal, return an empty string
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of the two strings
        gcd_length = math.gcd(len(str1), len(str2))
        
        # The GCD of the strings will be the prefix of either string with length gcd_length
        return str1[:gcd_length]