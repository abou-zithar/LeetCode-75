class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start =0 
        end = k
        counter = 0

        for letter in s[start:end]:
            if letter in "aeiou":
                counter +=1

        max_counter = counter

    
        while end < len(s):
            if s[start] in "aeiou":
                counter -=1
            if s[end] in "aeiou":
                counter +=1
            
            max_counter = max(max_counter,counter)

            if max_counter == k:
                return max_counter

            start +=1
            end +=1
        return max_counter
        


        
        