class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i=0
        word3 = [ ]
        while i < len(word1) or i< len(word2) :
            if i< len(word1):
                word3.append(word1[i])
            if i < len(word2):
                word3.append(word2[i])
            i+=1
        return "".join(word3)
        


        