class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i= 0
        j =0
        counter = len(s)

        if counter == 0:
            return True

        while j < len(t) and i < len(s):
            if s[i] == t[j] :
                counter -=1
                i+=1
            j+=1
        
        if counter == 0 :
            return True
        else:
            return False
   
            
            


        