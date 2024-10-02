class Solution:
    def compress(self, chars: List[str]) -> int:
        j= 0
        i =0
        while j < len(chars):
            current_char = chars[j]
            counter =0 
            while j < len(chars) and current_char == chars[j]:
                j+=1
                counter +=1
            chars[i] = current_char
            i+=1
            if counter > 1:
                for n in str(counter):
                    chars[i] = n
                    i+=1
        
        return i
