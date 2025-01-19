class Solution:

    
    def decodeString(self, s: str) -> str:
        stack = []  
        current_string = ""  
        current_num = 0  
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                last_string, repeat_num = stack.pop()
                current_string = last_string + current_string * repeat_num
            else:
                current_string += char

            print(stack)
    
        return current_string