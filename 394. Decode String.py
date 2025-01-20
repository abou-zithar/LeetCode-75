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
    



class Solution2:

    
    def decodeString(self, s: str) -> str:
        stack = []  
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                current_string = ""  

                while stack[-1] != "[":
                    current_string =   stack.pop() + current_string
                
                stack.pop()
                current_num = "" 
                while stack and stack[-1].isdigit():
                    current_num =   stack.pop() + current_num

                stack.append( int(current_num) * current_string)

        return "".join(stack)
        