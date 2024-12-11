from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c2 =Counter(word2)
        c1 =Counter(word1)
        return sorted(c1.values()) == sorted(c2.values()) and c1.keys() == c2.keys()